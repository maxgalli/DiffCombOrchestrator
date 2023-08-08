#!/bin/bash

# To make it work on T3
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch/
source $VO_CMS_SW_DIR/cmsset_default.sh

# Usual for Combine
ulimit -s unlimited

# Save root directory
export ROOTDIR="${PWD}"
export INSTALL_DIR="${PWD}/install_dir"

# pip install helper
custom_pip_install() {
    PYTHONUSERBASE="${INSTALL_DIR}" pip3 install --user --no-cache-dir --force-reinstall "$@"
}
[ ! -z "${BASH_VERSION}" ] && export -f custom_pip_install

set_pythonpath() {
    export PYTHONPATH="${PYTHONPATH}:${INSTALL_DIR}/lib/python3.8/site-packages"
    export PATH="${INSTALL_DIR}/bin:${PATH}"
}

# Check if the software is built for the first time
if [ -f ".built.txt" ]; then
    if [ "$1" = "clean" ]; then
        echo "Cleaning the software."
        # Perform actions for cleaning the software
        rm -rf CMSSW_11_3_4
        rm -rf .built.txt
        rm -rf $INSTALL_DIR
    else
        echo "Software has already been built. It needs to be sourced."
        # Perform actions for sourcing the software
        cd CMSSW_11_3_4/src
        cmsenv
        cd $ROOTDIR
        set_pythonpath
    fi
else 
    echo "Software is being built for the first time."
    # Perform actions for first time build
    # CMSSW, Combine, CombineHarvester
    cmsrel CMSSW_11_3_4
    cd CMSSW_11_3_4/src
    cmsenv
    git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
    cd HiggsAnalysis/CombinedLimit
    git remote add max git@github.com:maxgalli/HiggsAnalysis-CombinedLimit.git
    git fetch max
    git checkout max/DiffEFT_11_3_4_py3
    cd ../..
    git clone https://github.com/cms-analysis/CombineHarvester.git CombineHarvester
    cd CombineHarvester
    git checkout v2.0.0
    cd ..
    scram b -j
    cd $ROOTDIR

    # Main repo
    if [ ! -d "DifferentialCombinationRun2" ]; then
        git clone --recursive ssh://git@gitlab.cern.ch:7999/magalli/differentialcombinationrun2-2.git DifferentialCombinationRun2
        cd DifferentialCombinationRun2
        git checkout py3
        cd $ROOTDIR
    fi

    # Post process repo
    if [ ! -d "DifferentialCombinationPostProcess" ]; then
        git clone git@github.com:maxgalli/DifferentialCombinationPostProcess.git
    fi

    # Install python dependencies
    mkdir -p "${INSTALL_DIR}"
    custom_pip_install 'rich'
    custom_pip_install 'mplhep'
    custom_pip_install 'uproot'

    # Install custom packages
    cd DifferentialCombinationRun2
    custom_pip_install -e .
    cd $ROOTDIR
    cd DifferentialCombinationPostProcess
    custom_pip_install -e .
    cd $ROOTDIR
    set_pythonpath

    # Make outputs directory
    mkdir -p outputs

    # Create a file to mark that the software has been built
    touch .built.txt
fi