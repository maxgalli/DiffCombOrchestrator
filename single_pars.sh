#!/usr/bin/env bash

#SBATCH --job-name=best_fit_ctbre
#SBATCH --mem=10G
#SBATCH -t 11:50:00
#SBATCH --partition=standard
#SBATCH --output=240628_tmp/output_ctbre_%j.txt
#SBATCH --error=240628_tmp/error_ctbre_%j.txt

#submit_SMEFT_scans.py --chan-obs /work/gallim/DifferentialCombination_home/DiffCombOrchestrator/DifferentialCombinationRun2/metadata/SMEFT/config/PtFullComb2.json --category asimov --input-dir /work/gallim/DifferentialCombination_home/DiffCombOrchestrator/CombinedWorkspaces/SMEFT/CMS-ForDiff-230530/230620PruneNoCP --output-dir /work/gallim/DifferentialCombination_home/DiffCombOrchestrator/outputs/SMEFT_scans/230620PruneNoCP/FreezeOthers_ctbre/PtFullComb2_asimov-luigi --base-model /work/gallim/DifferentialCombination_home/DiffCombOrchestrator/DifferentialCombinationRun2/metadata/SMEFT/230620PruneNoCP.yml --submodel ctbre --skip-2d --crab --force-output-name
submit_SMEFT_scans.py --chan-obs /work/gallim/DifferentialCombination_home/DiffCombOrchestrator/DifferentialCombinationRun2/metadata/SMEFT/config/PtFullComb2.json --category asimov --input-dir /work/gallim/DifferentialCombination_home/DiffCombOrchestrator/CombinedWorkspaces/SMEFT/CMS-ForDiff-230530/230620PruneNoCP --output-dir /work/gallim/DifferentialCombination_home/DiffCombOrchestrator/outputs/SMEFT_scans --base-model /work/gallim/DifferentialCombination_home/DiffCombOrchestrator/DifferentialCombinationRun2/metadata/SMEFT/230620PruneNoCP.yml --submodel ctbre --skip-2d --crab
