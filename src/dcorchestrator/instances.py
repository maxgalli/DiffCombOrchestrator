import luigi
import os
from .utils import run_list_of_commands, BaseNotifierClass
from .tasks import (
    CombineCards,
    CreateSMWorkspace,
    SubmitSMScans,
    CreateKappaWorkspace,
    SubmitKappaScans,
    CreateSMEFTWorkspace,
    SubmitSMEFTScans,
)

root_dir = os.environ["ROOTDIR"]

"""
SM
"""

create_sm_workspace_pt_Hgg = CreateSMWorkspace(
    datacard_path="{}/DifferentialCombinationRun2/Analyses/hig-19-016-noprune/outdir_differential_Pt/Datacard_13TeV_differential_Pt.txt".format(
        root_dir
    ),
    observable="smH_PTH",
    category="Hgg",
)

submit_sm_scans_pt_Hgg = SubmitSMScans(
    category="Hgg",
    create_sm_workspace=create_sm_workspace_pt_Hgg,
)

submit_sm_scans_pt_Hgg_asimov = SubmitSMScans(
    category="Hgg_asimov",
    create_sm_workspace=create_sm_workspace_pt_Hgg,
)

create_sm_workspace_pt_HZZ = CreateSMWorkspace(
    datacard_path="DifferentialCombinationRun2/Analyses/hig-21-009/pT4l/hzz4l_all_13TeV_xs_pT4l_bin_v3.txt",
    observable="smH_PTH",
    category="HZZ",
)

submit_sm_scans_pt_HZZ = SubmitSMScans(
    category="HZZ",
    create_sm_workspace=create_sm_workspace_pt_HZZ,
    has_jobs=False,
)

submit_sm_scans_pt_HZZ_asimov = SubmitSMScans(
    category="HZZ_asimov",
    create_sm_workspace=create_sm_workspace_pt_HZZ,
    has_jobs=False,
)

create_sm_workspace_pt_HWW = CreateSMWorkspace(
    datacard_path="DifferentialCombinationRun2/Analyses/hig-19-002/ptH_for_differential_combination/fullmodel_unreg.txt",
    observable="smH_PTH",
    category="HWW",
)

submit_sm_scans_pt_HWW = SubmitSMScans(
    category="HWW",
    create_sm_workspace=create_sm_workspace_pt_HWW,
)

submit_sm_scans_pt_HWW_asimov = SubmitSMScans(
    category="HWW_asimov",
    create_sm_workspace=create_sm_workspace_pt_HWW,
)

create_sm_workspace_pt_Htt = CreateSMWorkspace(
    datacard_path="{}/DifferentialCombinationRun2/Analyses/hig-20-015/HiggsPt/HTT_Run2FinalCard_HiggsPt_NoReg.txt".format(
        root_dir
    ),
    observable="smH_PTH",
    category="Htt",
)

submit_sm_scans_pt_Htt = SubmitSMScans(
    category="Htt",
    create_sm_workspace=create_sm_workspace_pt_Htt,
)

submit_sm_scans_pt_Htt_asimov = SubmitSMScans(
    category="Htt_asimov",
    create_sm_workspace=create_sm_workspace_pt_Htt,
)

create_sm_workspace_pt_HttBoost = CreateSMWorkspace(
    datacard_path="{}/DifferentialCombinationRun2/Analyses/hig-21-017/BoostedHTT_DiffXS_HiggsPt_NoOverLap_New/Diff_V7_FreshRun_hpt_NoOverLap_rename/hig-21-017_hpt_forComb.txt".format(
        root_dir
    ),
    observable="smH_PTH",
    category="HttBoost",
)

submit_sm_scans_pt_HttBoost = SubmitSMScans(
    category="HttBoost",
    create_sm_workspace=create_sm_workspace_pt_HttBoost,
    has_jobs=False,
)

submit_sm_scans_pt_HttBoost_asimov = SubmitSMScans(
    category="HttBoost_asimov",
    create_sm_workspace=create_sm_workspace_pt_HttBoost,
    has_jobs=False,
)

create_sm_workspace_pt_HbbVBF = CreateSMWorkspace(
    datacard_path="{}/DifferentialCombinationRun2/Analyses/hig-21-020/signal-strength/testModel/model_combined_withpaths.txt".format(root_dir),
    observable="smH_PTH",
    category="HbbVBF",
)

submit_sm_scans_pt_HbbVBF = SubmitSMScans(
    category="HbbVBF",
    create_sm_workspace=create_sm_workspace_pt_HbbVBF,
)

submit_sm_scans_pt_HbbVBF_asimov = SubmitSMScans(
    category="HbbVBF_asimov",
    create_sm_workspace=create_sm_workspace_pt_HbbVBF,
)

combine_cards_sm_pt_HggHZZ = CombineCards(
    channels=[
        "hgg=DifferentialCombinationRun2/Analyses/hig-19-016/outdir_differential_Pt/Datacard_13TeV_differential_Pt.txt",
        "hzz=DifferentialCombinationRun2/Analyses/hig-21-009/pT4l/hzz4l_all_13TeV_xs_pT4l_bin_v3.txt",
    ],
    output_card_name="CombinedCards/smH_PTH/HggHZZ.txt",
)

create_sm_workspace_pt_HggHZZ = CreateSMWorkspace(
    datacard_path="{}/CombinedCards/smH_PTH/HggHZZ.txt".format(root_dir),
    observable="smH_PTH",
    category="HggHZZ",
    combine_cards=combine_cards_sm_pt_HggHZZ,
)

submit_sm_scans_pt_HggHZZ = SubmitSMScans(
    category="HggHZZ",
    create_sm_workspace=create_sm_workspace_pt_HggHZZ,
)

combine_cards_sm_pt_HggHZZHWWHttHttBoost = CombineCards(
    channels=[
        "hgg=DifferentialCombinationRun2/Analyses/hig-19-016-noprune/outdir_differential_Pt/Datacard_13TeV_differential_Pt.txt",
        "hzz=DifferentialCombinationRun2/Analyses/hig-21-009/pT4l/hzz4l_all_13TeV_xs_pT4l_bin_v3.txt",
        "hww=DifferentialCombinationRun2/Analyses/hig-19-002/ptH_for_differential_combination/fullmodel_unreg.txt",
        "htt=DifferentialCombinationRun2/Analyses/hig-20-015/HiggsPt/HTT_Run2FinalCard_HiggsPt_NoReg_swapOOA.txt",
        "httboost=DifferentialCombinationRun2/Analyses/hig-21-017/BoostedHTT_DiffXS_HiggsPt_NoOverLap_New/Diff_V7_FreshRun_hpt_NoOverLap_rename/all_swapOOA.txt"
    ],
    output_card_name="CombinedCards/smH_PTH/HggHZZHWWHttHttBoost.txt",
    replace_mass=True
)

combine_cards_sm_pt_HggHZZHWWHttHbbVBFHttBoost = CombineCards(
    channels=[
        "hgg=DifferentialCombinationRun2/Analyses/hig-19-016-noprune/outdir_differential_Pt/Datacard_13TeV_differential_Pt.txt",
        "hzz=DifferentialCombinationRun2/Analyses/hig-21-009/pT4l/hzz4l_all_13TeV_xs_pT4l_bin_v3.txt",
        "hww=DifferentialCombinationRun2/Analyses/hig-19-002/ptH_for_differential_combination/fullmodel_unreg.txt",
        "htt=DifferentialCombinationRun2/Analyses/hig-20-015/HiggsPt/HTT_Run2FinalCard_HiggsPt_NoReg_swapOOA.txt",
        "hbbvbf=DifferentialCombinationRun2/Analyses/hig-21-020/signal-strength/testModel/model_combined_withpaths_noVBF.txt",
        "httboost=DifferentialCombinationRun2/Analyses/hig-21-017/BoostedHTT_DiffXS_HiggsPt_NoOverLap_New/Diff_V7_FreshRun_hpt_NoOverLap_rename/all_swapOOA.txt"
    ],
    output_card_name="CombinedCards/smH_PTH/HggHZZHWWHttHbbVBFHttBoost.txt",
    replace_mass=True
)

combine_cards_sm_pt_FinalComb = CombineCards(
    channels=[
        "hgg=DifferentialCombinationRun2/Analyses/hig-19-016-noprune/outdir_differential_Pt/Datacard_13TeV_differential_Pt.txt",
        "hzz=DifferentialCombinationRun2/Analyses/hig-21-009/pT4l/hzz4l_all_13TeV_xs_pT4l_bin_v3.txt",
        "hww=DifferentialCombinationRun2/Analyses/hig-19-002/ptH_for_differential_combination/fullmodel_unreg.txt",
        "htt=DifferentialCombinationRun2/Analyses/hig-20-015/HiggsPt/HTT_Run2FinalCard_HiggsPt_NoReg_swapOOA.txt",
        "hbbvbf=DifferentialCombinationRun2/Analyses/hig-21-020/signal-strength/testModel/model_combined_withpaths_noVBF.txt",
        #"hbbvbf=DifferentialCombinationRun2/Analyses/hig-21-020/signal-strength/testModel/model_combined_withpaths.txt",
        "httboost=DifferentialCombinationRun2/Analyses/hig-21-017/BoostedHTT_DiffXS_HiggsPt_NoOverLap_New/Diff_V7_FreshRun_hpt_NoOverLap_rename/all_swapOOA.txt"
    ],
    output_card_name="CombinedCards/smH_PTH/FinalComb.txt",
    replace_mass=True
)

create_sm_workspace_pt_HggHZZHWWHttHttBoost = CreateSMWorkspace(
    datacard_path="{}/CombinedCards/smH_PTH/HggHZZHWWHttHttBoost.txt".format(root_dir),
    observable="smH_PTH",
    category="HggHZZHWWHttHttBoost",
    combine_cards=combine_cards_sm_pt_HggHZZHWWHttHttBoost,
)

create_sm_workspace_pt_HggHZZHWWHttHbbVBFHttBoost = CreateSMWorkspace(
    datacard_path="{}/CombinedCards/smH_PTH/HggHZZHWWHttHbbVBFHttBoost.txt".format(root_dir),
    observable="smH_PTH",
    category="HggHZZHWWHttHbbVBFHttBoost",
    combine_cards=combine_cards_sm_pt_HggHZZHWWHttHbbVBFHttBoost,
)

create_sm_workspace_pt_FinalComb = CreateSMWorkspace(
    datacard_path="{}/CombinedCards/smH_PTH/FinalComb.txt".format(root_dir),
    observable="smH_PTH",
    category="FinalComb",
    combine_cards=combine_cards_sm_pt_FinalComb,
)

submit_sm_scans_pt_HggHZZHWWHttHttBoost = SubmitSMScans(
    category="HggHZZHWWHttHttBoost",
    create_sm_workspace=create_sm_workspace_pt_HggHZZHWWHttHttBoost,
)

submit_sm_scans_pt_HggHZZHWWHttHbbVBFHttBoost = SubmitSMScans(
    category="HggHZZHWWHttHbbVBFHttBoost",
    create_sm_workspace=create_sm_workspace_pt_HggHZZHWWHttHbbVBFHttBoost,
)

submit_sm_scans_pt_HggHZZHWWHttHbbVBFHttBoost_asimov = SubmitSMScans(
    category="HggHZZHWWHttHbbVBFHttBoost_asimov",
    create_sm_workspace=create_sm_workspace_pt_HggHZZHWWHttHbbVBFHttBoost,
)

submit_sm_scans_pt_HggHZZHWWHttHbbVBFHttBoost_asimov_statonly = SubmitSMScans(
    category="HggHZZHWWHttHbbVBFHttBoost_asimov_statonly",
    create_sm_workspace=create_sm_workspace_pt_HggHZZHWWHttHbbVBFHttBoost,
    full_stat_task=submit_sm_scans_pt_HggHZZHWWHttHbbVBFHttBoost_asimov,
    global_fit_file="higgsCombineAsimovPostFit.GenerateOnly.mH125.38.123456.root"
)

submit_sm_scans_pt_FinalComb = SubmitSMScans(
    category="FinalComb",
    create_sm_workspace=create_sm_workspace_pt_FinalComb,
)

submit_sm_scans_pt_FinalComb_statonly = SubmitSMScans(
    category="FinalComb_statonly",
    create_sm_workspace=create_sm_workspace_pt_FinalComb,
    full_stat_task=submit_sm_scans_pt_FinalComb,
    global_fit_file="higgsCombine_POSTFIT_FinalComb.MultiDimFit.mH125.38.root",
)

submit_sm_scans_pt_FinalComb_asimov = SubmitSMScans(
    category="FinalComb_asimov",
    create_sm_workspace=create_sm_workspace_pt_FinalComb,
)

submit_sm_scans_pt_FinalComb_asimov_statonly = SubmitSMScans(
    category="FinalComb_asimov_statonly",
    create_sm_workspace=create_sm_workspace_pt_FinalComb,
    full_stat_task=submit_sm_scans_pt_FinalComb_asimov,
    global_fit_file="higgsCombineAsimovPostFit.GenerateOnly.mH125.38.123456.root"
)

create_sm_workspace_Njets_Hgg = CreateSMWorkspace(
    datacard_path="{}/DifferentialCombinationRun2/Analyses/hig-19-016/outdir_differential_Njets2p5/Datacard_13TeV_differential_Njets2p5.txt".format(root_dir),
    observable="Njets",
    category="Hgg",
)

submit_sm_scans_Njets_Hgg = SubmitSMScans(
    category="Hgg",
    create_sm_workspace=create_sm_workspace_Njets_Hgg,
)

submit_sm_scans_Njets_Hgg_asimov = SubmitSMScans(
    category="Hgg_asimov",
    create_sm_workspace=create_sm_workspace_Njets_Hgg,
)

create_sm_workspace_Njets_HZZ = CreateSMWorkspace(
    datacard_path="{}/DifferentialCombinationRun2/Analyses/hig-21-009/njets_pt30_eta4p7/hzz4l_all_13TeV_xs_njets_pt30_eta4p7_bin_v3.txt".format(root_dir),
    observable="Njets",
    category="HZZ",
)

submit_sm_scans_Njets_HZZ = SubmitSMScans(
    category="HZZ",
    has_jobs=False,
    create_sm_workspace=create_sm_workspace_Njets_HZZ,
)

submit_sm_scans_Njets_HZZ_asimov = SubmitSMScans(
    category="HZZ_asimov",
    has_jobs=False,
    create_sm_workspace=create_sm_workspace_Njets_HZZ,
)

create_sm_workspace_Njets_HWW = CreateSMWorkspace(
    datacard_path="{}/DifferentialCombinationRun2/Analyses/hig-19-002/njet/fullmodel.txt".format(root_dir),
    observable="Njets",
    category="HWW",
)

submit_sm_scans_Njets_HWW = SubmitSMScans(
    category="HWW",
    create_sm_workspace=create_sm_workspace_Njets_HWW,
)

submit_sm_scans_Njets_HWW_asimov = SubmitSMScans(
    category="HWW_asimov",
    create_sm_workspace=create_sm_workspace_Njets_HWW,
)

create_sm_workspace_Njets_Htt = CreateSMWorkspace(
    datacard_path="{}/DifferentialCombinationRun2/Analyses/hig-20-015/NJets/HTT_Run2FinalCard_NJets_AddedReg.txt".format(root_dir),
    observable="Njets",
    category="Htt",
)

submit_sm_scans_Njets_Htt = SubmitSMScans(
    category="Htt",
    create_sm_workspace=create_sm_workspace_Njets_Htt,
)

submit_sm_scans_Njets_Htt_asimov = SubmitSMScans(
    category="Htt_asimov",
    create_sm_workspace=create_sm_workspace_Njets_Htt,
)

combine_cards_sm_Njets_HggHZZHWWHtt = CombineCards(
    channels=[
        "hgg=DifferentialCombinationRun2/Analyses/hig-19-016/outdir_differential_Njets2p5/Datacard_13TeV_differential_Njets2p5.txt",
        "hzz=DifferentialCombinationRun2/Analyses/hig-21-009/njets_pt30_eta4p7/hzz4l_all_13TeV_xs_njets_pt30_eta4p7_bin_v3.txt",
        "hww=DifferentialCombinationRun2/Analyses/hig-19-002/njet/fullmodel.txt",
        "htt=DifferentialCombinationRun2/Analyses/hig-20-015/NJets/HTT_Run2FinalCard_NJets_NoReg.txt",
    ],
    output_card_name="{}/CombinedCards/Njets/HggHZZHWWHtt.txt".format(root_dir),
)

create_sm_workspace_Njets_HggHZZHWWHtt = CreateSMWorkspace(
    datacard_path="{}/CombinedCards/Njets/HggHZZHWWHtt.txt".format(root_dir),
    observable="Njets",
    category="HggHZZHWWHtt",
    combine_cards=combine_cards_sm_Njets_HggHZZHWWHtt,
)

submit_sm_scans_Njets_HggHZZHWWHtt = SubmitSMScans(
    category="HggHZZHWWHtt",
    create_sm_workspace=create_sm_workspace_Njets_HggHZZHWWHtt,
)

submit_sm_scans_Njets_HggHZZHWWHtt_statonly = SubmitSMScans(
    category="HggHZZHWWHtt_statonly",
    create_sm_workspace=create_sm_workspace_Njets_HggHZZHWWHtt,
    full_stat_task=submit_sm_scans_Njets_HggHZZHWWHtt,
    global_fit_file="higgsCombine_POSTFIT_HggHZZHWWHtt.MultiDimFit.mH125.38.root",
)

submit_sm_scans_Njets_HggHZZHWWHtt_asimov = SubmitSMScans(
    category="HggHZZHWWHtt_asimov",
    create_sm_workspace=create_sm_workspace_Njets_HggHZZHWWHtt,
)

submit_sm_scans_Njets_HggHZZHWWHtt_asimov_statonly = SubmitSMScans(
    category="HggHZZHWWHtt_asimov_statonly",
    create_sm_workspace=create_sm_workspace_Njets_HggHZZHWWHtt,
    full_stat_task=submit_sm_scans_Njets_HggHZZHWWHtt_asimov,
    global_fit_file="higgsCombineAsimovPostFit.GenerateOnly.mH125.38.123456.root",
)

create_sm_workspace_yH_Hgg = CreateSMWorkspace(
    datacard_path="{}/DifferentialCombinationRun2/Analyses/hig-19-016/outdir_differential_AbsRapidityFine/Datacard_13TeV_differential_AbsRapidityFine.txt".format(root_dir),
    observable="yH",
    category="Hgg",
)

submit_sm_scans_yH_Hgg = SubmitSMScans(
    category="Hgg",
    create_sm_workspace=create_sm_workspace_yH_Hgg,
)

submit_sm_scans_yH_Hgg_asimov = SubmitSMScans(
    category="Hgg_asimov",
    create_sm_workspace=create_sm_workspace_yH_Hgg,
)

create_sm_workspace_yH_HZZ = CreateSMWorkspace(
    datacard_path="{}/DifferentialCombinationRun2/Analyses/hig-21-009/rapidity4l/hzz4l_all_13TeV_xs_rapidity4l_bin_v3.txt".format(root_dir),
    observable="yH",
    category="HZZ",
)

submit_sm_scans_yH_HZZ = SubmitSMScans(
    category="HZZ",
    has_jobs=False,
    create_sm_workspace=create_sm_workspace_yH_HZZ,
)

submit_sm_scans_yH_HZZ_asimov = SubmitSMScans(
    category="HZZ_asimov",
    has_jobs=False,
    create_sm_workspace=create_sm_workspace_yH_HZZ,
)

combine_cards_sm_yH_HggHZZ = CombineCards(
    channels=[
        "hgg=DifferentialCombinationRun2/Analyses/hig-19-016/outdir_differential_AbsRapidityFine/Datacard_13TeV_differential_AbsRapidityFine.txt",
        "hzz=DifferentialCombinationRun2/Analyses/hig-21-009/rapidity4l/hzz4l_all_13TeV_xs_rapidity4l_bin_v3.txt",
    ],
    output_card_name="{}/CombinedCards/yH/HggHZZ.txt".format(root_dir),
)

create_sm_workspace_yH_HggHZZ = CreateSMWorkspace(
    datacard_path="{}/CombinedCards/yH/HggHZZ.txt".format(root_dir),
    observable="yH",
    category="HggHZZ",
    combine_cards=combine_cards_sm_yH_HggHZZ,
)

submit_sm_scans_yH_HggHZZ = SubmitSMScans(
    category="HggHZZ",
    create_sm_workspace=create_sm_workspace_yH_HggHZZ,
)

submit_sm_scans_yH_HggHZZ_statonly = SubmitSMScans(
    category="HggHZZ_statonly",
    create_sm_workspace=create_sm_workspace_yH_HggHZZ,
    full_stat_task=submit_sm_scans_yH_HggHZZ,
    global_fit_file="higgsCombine_POSTFIT_HggHZZ.MultiDimFit.mH125.38.root",
)

submit_sm_scans_yH_HggHZZ_asimov = SubmitSMScans(
    category="HggHZZ_asimov",
    create_sm_workspace=create_sm_workspace_yH_HggHZZ,
)

submit_sm_scans_yH_HggHZZ_asimov_statonly = SubmitSMScans(
    category="HggHZZ_asimov_statonly",
    create_sm_workspace=create_sm_workspace_yH_HggHZZ,
    full_stat_task=submit_sm_scans_yH_HggHZZ_asimov,
    global_fit_file="higgsCombineAsimovPostFit.GenerateOnly.mH125.38.123456.root",
)

create_sm_workspace_ptj_Hgg = CreateSMWorkspace(
    datacard_path="{}/DifferentialCombinationRun2/Analyses/hig-19-016/outdir_differential_Jet2p5Pt0/Datacard_13TeV_differential_Jet2p5Pt0.txt".format(root_dir),
    observable="smH_PTJ0",
    category="Hgg",
)

submit_sm_scans_ptj_Hgg = SubmitSMScans(
    category="Hgg",
    create_sm_workspace=create_sm_workspace_ptj_Hgg,
)

submit_sm_scans_ptj_Hgg_asimov = SubmitSMScans(
    category="Hgg_asimov",
    create_sm_workspace=create_sm_workspace_ptj_Hgg,
)

create_sm_workspace_ptj_HZZ = CreateSMWorkspace(
    datacard_path="{}/DifferentialCombinationRun2/Analyses/hig-21-009/pTj1/hzz4l_all_13TeV_xs_pTj1_bin_v3.txt".format(root_dir),
    observable="smH_PTJ0",
    category="HZZ",
)

submit_sm_scans_ptj_HZZ = SubmitSMScans(
    category="HZZ",
    has_jobs=False,
    create_sm_workspace=create_sm_workspace_ptj_HZZ,
)

submit_sm_scans_ptj_HZZ_asimov = SubmitSMScans(
    category="HZZ_asimov",
    has_jobs=False,
    create_sm_workspace=create_sm_workspace_ptj_HZZ,
)

create_sm_workspace_ptj_HttBoost = CreateSMWorkspace(
    datacard_path="{}/DifferentialCombinationRun2/Analyses/hig-21-017/BoostedHTT_DiffXS_LeadJetPt_NoOverLap_New/Diff_V7_FreshRun_jpt_NoOverLap_rename/hig-21-017_jpt_forComb.txt".format(root_dir),
    observable="smH_PTJ0",
    category="HttBoost",
)

submit_sm_scans_ptj_HttBoost = SubmitSMScans(
    category="HttBoost",
    create_sm_workspace=create_sm_workspace_ptj_HttBoost,
    has_jobs=False,
)

submit_sm_scans_ptj_HttBoost_asimov = SubmitSMScans(
    category="HttBoost_asimov",
    create_sm_workspace=create_sm_workspace_ptj_HttBoost,
    has_jobs=False,
)

combine_cards_sm_ptj_HggHZZHttBoost = CombineCards(
    channels=[
        "hgg=DifferentialCombinationRun2/Analyses/hig-19-016/outdir_differential_Jet2p5Pt0/Datacard_13TeV_differential_Jet2p5Pt0.txt",
        "hzz=DifferentialCombinationRun2/Analyses/hig-21-009/pTj1/hzz4l_all_13TeV_xs_pTj1_bin_v3.txt",
        "httboost=DifferentialCombinationRun2/Analyses/hig-21-017/BoostedHTT_DiffXS_HiggsPt_NoOverLap_New/Diff_V7_FreshRun_hpt_NoOverLap_rename/all.txt",
    ],
    output_card_name="{}/CombinedCards/smH_PTJ0/HggHZZHttBoost.txt".format(root_dir),
    replace_mass=True
)

create_sm_workspace_ptj_HggHZZHttBoost = CreateSMWorkspace(
    datacard_path="{}/CombinedCards/smH_PTJ0/HggHZZHttBoost.txt".format(root_dir),
    observable="smH_PTJ0",
    category="HggHZZHttBoost",
    combine_cards=combine_cards_sm_ptj_HggHZZHttBoost,
)

create_sm_workspace_ptj_FinalComb = CreateSMWorkspace(
    datacard_path="{}/CombinedCards/smH_PTJ0/HggHZZHttBoost.txt".format(root_dir),
    observable="smH_PTJ0",
    category="FinalComb",
    combine_cards=combine_cards_sm_ptj_HggHZZHttBoost,
)

submit_sm_scans_ptj_HggHZZHttBoost = SubmitSMScans(
    category="HggHZZHttBoost",
    create_sm_workspace=create_sm_workspace_ptj_HggHZZHttBoost,
)

submit_sm_scans_ptj_HggHZZHttBoost_statonly = SubmitSMScans(
    category="HggHZZHttBoost_statonly",
    create_sm_workspace=create_sm_workspace_ptj_HggHZZHttBoost,
    full_stat_task=submit_sm_scans_ptj_HggHZZHttBoost,
    global_fit_file="higgsCombine_POSTFIT_HggHZZHttBoost.MultiDimFit.mH125.38.root",
)

submit_sm_scans_ptj_HggHZZHttBoost_asimov = SubmitSMScans(
    category="HggHZZHttBoost_asimov",
    create_sm_workspace=create_sm_workspace_ptj_HggHZZHttBoost,
)

submit_sm_scans_ptj_HggHZZHttBoost_asimov_statonly = SubmitSMScans(
    category="HggHZZHttBoost_asimov_statonly",
    create_sm_workspace=create_sm_workspace_ptj_HggHZZHttBoost,
    full_stat_task=submit_sm_scans_ptj_HggHZZHttBoost_asimov,
    global_fit_file="higgsCombineAsimovPostFit.GenerateOnly.mH125.38.123456.root"
)

submit_sm_scans_ptj_FinalComb = SubmitSMScans(
    category="FinalComb",
    create_sm_workspace=create_sm_workspace_ptj_FinalComb,
)

submit_sm_scans_ptj_FinalComb_statonly = SubmitSMScans(
    category="FinalComb_statonly",
    create_sm_workspace=create_sm_workspace_ptj_FinalComb,
    full_stat_task=submit_sm_scans_ptj_FinalComb,
    global_fit_file="higgsCombine_POSTFIT_FinalComb.MultiDimFit.mH125.38.root",
)

submit_sm_scans_ptj_FinalComb_asimov = SubmitSMScans(
    category="FinalComb_asimov",
    create_sm_workspace=create_sm_workspace_ptj_FinalComb,
)

submit_sm_scans_ptj_FinalComb_asimov_statonly = SubmitSMScans(
    category="FinalComb_asimov_statonly",
    create_sm_workspace=create_sm_workspace_ptj_FinalComb,
    full_stat_task=submit_sm_scans_ptj_FinalComb_asimov,
    global_fit_file="higgsCombineAsimovPostFit.GenerateOnly.mH125.38.123456.root"
)

create_sm_workspace_mjj_Hgg = CreateSMWorkspace(
    datacard_path="{}/DifferentialCombinationRun2/Analyses/hig-19-016/outdir_differential_MjjJets4p7NewBins/Datacard_13TeV_differential_MjjJets4p7NewBins.txt".format(root_dir),
    observable="mjj",
    category="Hgg",
)

submit_sm_scans_mjj_Hgg = SubmitSMScans(
    category="Hgg",
    create_sm_workspace=create_sm_workspace_mjj_Hgg,
)

submit_sm_scans_mjj_Hgg_asimov = SubmitSMScans(
    category="Hgg_asimov",
    create_sm_workspace=create_sm_workspace_mjj_Hgg,
)

create_sm_workspace_mjj_HZZ = CreateSMWorkspace(
    datacard_path="{}/DifferentialCombinationRun2/Analyses/hig-21-009/mjj/hzz4l_all_13TeV_xs_mjj_bin_v3.txt".format(root_dir),
    observable="mjj",
    category="HZZ",
)

submit_sm_scans_mjj_HZZ = SubmitSMScans(
    category="HZZ",
    has_jobs=False,
    create_sm_workspace=create_sm_workspace_mjj_HZZ,
)

submit_sm_scans_mjj_HZZ_asimov = SubmitSMScans(
    category="HZZ_asimov",
    has_jobs=False,
    create_sm_workspace=create_sm_workspace_mjj_HZZ,
)

combine_cards_sm_mjj_HggHZZ = CombineCards(
    channels=[
        "hgg=DifferentialCombinationRun2/Analyses/hig-19-016/outdir_differential_MjjJets4p7NewBins/Datacard_13TeV_differential_MjjJets4p7NewBins.txt",
        "hzz=DifferentialCombinationRun2/Analyses/hig-21-009/mjj/hzz4l_all_13TeV_xs_mjj_bin_v3.txt",
    ],
    output_card_name="{}/CombinedCards/mjj/HggHZZ.txt".format(root_dir),
)

create_sm_workspace_mjj_HggHZZ = CreateSMWorkspace(
    datacard_path="{}/CombinedCards/mjj/HggHZZ.txt".format(root_dir),
    observable="mjj",
    category="HggHZZ",
    combine_cards=combine_cards_sm_mjj_HggHZZ,
)

submit_sm_scans_mjj_HggHZZ = SubmitSMScans(
    category="HggHZZ",
    create_sm_workspace=create_sm_workspace_mjj_HggHZZ,
)

submit_sm_scans_mjj_HggHZZ_statonly = SubmitSMScans(
    category="HggHZZ_statonly",
    create_sm_workspace=create_sm_workspace_mjj_HggHZZ,
    full_stat_task=submit_sm_scans_mjj_HggHZZ,
    global_fit_file="higgsCombine_POSTFIT_HggHZZ.MultiDimFit.mH125.38.root",
)

submit_sm_scans_mjj_HggHZZ_asimov = SubmitSMScans(
    category="HggHZZ_asimov",
    create_sm_workspace=create_sm_workspace_mjj_HggHZZ,
)

submit_sm_scans_mjj_HggHZZ_asimov_statonly = SubmitSMScans(
    category="HggHZZ_asimov_statonly",
    create_sm_workspace=create_sm_workspace_mjj_HggHZZ,
    full_stat_task=submit_sm_scans_mjj_HggHZZ_asimov,
    global_fit_file="higgsCombineAsimovPostFit.GenerateOnly.mH125.38.123456.root"
)

create_sm_workspace_detajj_Hgg = CreateSMWorkspace(
    datacard_path="{}/DifferentialCombinationRun2/Analyses/hig-19-016/outdir_differential_AbsDeltaEtaJ1J2Jets4p7/Datacard_13TeV_differential_AbsDeltaEtaJ1J2Jets4p7.txt".format(root_dir),
    observable="DEtajj",
    category="Hgg",
)

submit_sm_scans_detajj_Hgg = SubmitSMScans(
    category="Hgg",
    create_sm_workspace=create_sm_workspace_detajj_Hgg,
)

submit_sm_scans_detajj_Hgg_asimov = SubmitSMScans(
    category="Hgg_asimov",
    create_sm_workspace=create_sm_workspace_detajj_Hgg,
)

create_sm_workspace_detajj_HZZ = CreateSMWorkspace(
    datacard_path="{}/DifferentialCombinationRun2/Analyses/hig-21-009/absdetajj/hzz4l_all_13TeV_xs_absdetajj_bin_v3.txt".format(root_dir),
    observable="DEtajj",
    category="HZZ",
)

submit_sm_scans_detajj_HZZ = SubmitSMScans(
    category="HZZ",
    has_jobs=False,
    create_sm_workspace=create_sm_workspace_detajj_HZZ,
)

submit_sm_scans_detajj_HZZ_asimov = SubmitSMScans(
    category="HZZ_asimov",
    has_jobs=False,
    create_sm_workspace=create_sm_workspace_detajj_HZZ,
)

combine_cards_sm_detajj_HggHZZ = CombineCards(
    channels=[
        "hgg=DifferentialCombinationRun2/Analyses/hig-19-016/outdir_differential_AbsDeltaEtaJ1J2Jets4p7/Datacard_13TeV_differential_AbsDeltaEtaJ1J2Jets4p7.txt",
        "hzz=DifferentialCombinationRun2/Analyses/hig-21-009/absdetajj/hzz4l_all_13TeV_xs_absdetajj_bin_v3.txt",
    ],
    output_card_name="{}/CombinedCards/DEtajj/HggHZZ.txt".format(root_dir),
)

create_sm_workspace_detajj_HggHZZ = CreateSMWorkspace(
    datacard_path="{}/CombinedCards/DEtajj/HggHZZ.txt".format(root_dir),
    observable="DEtajj",
    category="HggHZZ",
    combine_cards=combine_cards_sm_detajj_HggHZZ,
)

submit_sm_scans_detajj_HggHZZ = SubmitSMScans(
    category="HggHZZ",
    create_sm_workspace=create_sm_workspace_detajj_HggHZZ,
)

submit_sm_scans_detajj_HggHZZ_statonly = SubmitSMScans(
    category="HggHZZ_statonly",
    create_sm_workspace=create_sm_workspace_detajj_HggHZZ,
    full_stat_task=submit_sm_scans_detajj_HggHZZ,
    global_fit_file="higgsCombine_POSTFIT_HggHZZ.MultiDimFit.mH125.38.root",
)

submit_sm_scans_detajj_HggHZZ_asimov = SubmitSMScans(
    category="HggHZZ_asimov",
    create_sm_workspace=create_sm_workspace_detajj_HggHZZ,
)

submit_sm_scans_detajj_HggHZZ_asimov_statonly = SubmitSMScans(
    category="HggHZZ_asimov_statonly",
    create_sm_workspace=create_sm_workspace_detajj_HggHZZ,
    full_stat_task=submit_sm_scans_detajj_HggHZZ_asimov,
    global_fit_file="higgsCombineAsimovPostFit.GenerateOnly.mH125.38.123456.root"
)

create_sm_workspace_taucj_Hgg = CreateSMWorkspace(
    datacard_path="{}/DifferentialCombinationRun2/Analyses/hig-19-016/outdir_differential_TauCJets4p7/Datacard_13TeV_differential_TauCJets4p7.txt".format(root_dir),
    observable="TauCJ",
    category="Hgg",
)

submit_sm_scans_taucj_Hgg = SubmitSMScans(
    category="Hgg",
    create_sm_workspace=create_sm_workspace_taucj_Hgg,
)

submit_sm_scans_taucj_Hgg_asimov = SubmitSMScans(
    category="Hgg_asimov",
    create_sm_workspace=create_sm_workspace_taucj_Hgg,
)

create_sm_workspace_taucj_HZZ = CreateSMWorkspace(
    datacard_path="{}/DifferentialCombinationRun2/Analyses/hig-21-009/TCjmax/hzz4l_all_13TeV_xs_TCjmax_bin_v3.txt".format(root_dir),
    observable="TauCJ",
    category="HZZ",
)

submit_sm_scans_taucj_HZZ = SubmitSMScans(
    category="HZZ",
    has_jobs=False,
    create_sm_workspace=create_sm_workspace_taucj_HZZ,
)

submit_sm_scans_taucj_HZZ_asimov = SubmitSMScans(
    category="HZZ_asimov",
    has_jobs=False,
    create_sm_workspace=create_sm_workspace_taucj_HZZ,
)

combine_cards_sm_taucj_HggHZZ = CombineCards(
    channels=[
        "hgg=DifferentialCombinationRun2/Analyses/hig-19-016/outdir_differential_TauCJets4p7/Datacard_13TeV_differential_TauCJets4p7.txt",
        "hzz=DifferentialCombinationRun2/Analyses/hig-21-009/TCjmax/hzz4l_all_13TeV_xs_TCjmax_bin_v3.txt",
    ],
    output_card_name="{}/CombinedCards/TauCJ/HggHZZ.txt".format(root_dir),
)

create_sm_workspace_taucj_HggHZZ = CreateSMWorkspace(
    datacard_path="{}/CombinedCards/TauCJ/HggHZZ.txt".format(root_dir),
    observable="TauCJ",
    category="HggHZZ",
    combine_cards=combine_cards_sm_taucj_HggHZZ,
)

submit_sm_scans_taucj_HggHZZ = SubmitSMScans(
    category="HggHZZ",
    create_sm_workspace=create_sm_workspace_taucj_HggHZZ,
)

submit_sm_scans_taucj_HggHZZ_statonly = SubmitSMScans(
    category="HggHZZ_statonly",
    create_sm_workspace=create_sm_workspace_taucj_HggHZZ,
    full_stat_task=submit_sm_scans_taucj_HggHZZ,
    global_fit_file="higgsCombine_POSTFIT_HggHZZ.MultiDimFit.mH125.38.root",
)

submit_sm_scans_taucj_HggHZZ_asimov = SubmitSMScans(
    category="HggHZZ_asimov",
    create_sm_workspace=create_sm_workspace_taucj_HggHZZ,
)

submit_sm_scans_taucj_HggHZZ_asimov_statonly = SubmitSMScans(
    category="HggHZZ_asimov_statonly",
    create_sm_workspace=create_sm_workspace_taucj_HggHZZ,
    full_stat_task=submit_sm_scans_taucj_HggHZZ_asimov,
    global_fit_file="higgsCombineAsimovPostFit.GenerateOnly.mH125.38.123456.root"
)

submit_instances = {
    "SM_pt_Hgg": submit_sm_scans_pt_Hgg,
    "SM_pt_Hgg_asimov": submit_sm_scans_pt_Hgg_asimov,
    "SM_pt_HZZ": submit_sm_scans_pt_HZZ,
    "SM_pt_HZZ_asimov": submit_sm_scans_pt_HZZ_asimov,
    "SM_pt_HWW": submit_sm_scans_pt_HWW,
    "SM_pt_HWW_asimov": submit_sm_scans_pt_HWW_asimov,
    "SM_pt_Htt": submit_sm_scans_pt_Htt,
    "SM_pt_Htt_asimov": submit_sm_scans_pt_Htt_asimov,
    "SM_pt_HttBoost": submit_sm_scans_pt_HttBoost,
    "SM_pt_HttBoost_asimov": submit_sm_scans_pt_HttBoost_asimov,
    "SM_pt_HbbVBF": submit_sm_scans_pt_HbbVBF,
    "SM_pt_HbbVBF_asimov": submit_sm_scans_pt_HbbVBF_asimov,
    "SM_pt_HggHZZ": submit_sm_scans_pt_HggHZZ,
    "SM_pt_HggHZZHWWHttHbbVBFHttBoost": submit_sm_scans_pt_HggHZZHWWHttHbbVBFHttBoost,
    "SM_pt_HggHZZHWWHttHbbVBFHttBoost_asimov": submit_sm_scans_pt_HggHZZHWWHttHbbVBFHttBoost_asimov,
    "SM_pt_HggHZZHWWHttHbbVBFHttBoost_asimov_statonly": submit_sm_scans_pt_HggHZZHWWHttHbbVBFHttBoost_asimov_statonly,
    "SM_pt_FinalComb": submit_sm_scans_pt_FinalComb,
    "SM_pt_FinalComb_statonly": submit_sm_scans_pt_FinalComb_statonly,
    "SM_pt_FinalComb_asimov": submit_sm_scans_pt_FinalComb_asimov,
    "SM_pt_FinalComb_asimov_statonly": submit_sm_scans_pt_FinalComb_asimov_statonly,
    "SM_Njets_Hgg": submit_sm_scans_Njets_Hgg,
    "SM_Njets_Hgg_asimov": submit_sm_scans_Njets_Hgg_asimov,
    "SM_Njets_HZZ": submit_sm_scans_Njets_HZZ,
    "SM_Njets_HZZ_asimov": submit_sm_scans_Njets_HZZ_asimov,
    "SM_Njets_HWW": submit_sm_scans_Njets_HWW,
    "SM_Njets_HWW_asimov": submit_sm_scans_Njets_HWW_asimov,
    "SM_Njets_Htt": submit_sm_scans_Njets_Htt,
    "SM_Njets_Htt_asimov": submit_sm_scans_Njets_Htt_asimov,
    "SM_Njets_HggHZZHWWHtt": submit_sm_scans_Njets_HggHZZHWWHtt,
    "SM_Njets_HggHZZHWWHtt_statonly": submit_sm_scans_Njets_HggHZZHWWHtt_statonly,
    "SM_Njets_HggHZZHWWHtt_asimov": submit_sm_scans_Njets_HggHZZHWWHtt_asimov,
    "SM_Njets_HggHZZHWWHtt_asimov_statonly": submit_sm_scans_Njets_HggHZZHWWHtt_asimov_statonly,
    "SM_yH_Hgg": submit_sm_scans_yH_Hgg,
    "SM_yH_Hgg_asimov": submit_sm_scans_yH_Hgg_asimov,
    "SM_yH_HZZ": submit_sm_scans_yH_HZZ,
    "SM_yH_HZZ_asimov": submit_sm_scans_yH_HZZ_asimov,
    "SM_yH_HggHZZ": submit_sm_scans_yH_HggHZZ,
    "SM_yH_HggHZZ_statonly": submit_sm_scans_yH_HggHZZ_statonly,
    "SM_yH_HggHZZ_asimov": submit_sm_scans_yH_HggHZZ_asimov,
    "SM_yH_HggHZZ_asimov_statonly": submit_sm_scans_yH_HggHZZ_asimov_statonly,
    "SM_ptj_Hgg": submit_sm_scans_ptj_Hgg,
    "SM_ptj_Hgg_asimov": submit_sm_scans_ptj_Hgg_asimov,
    "SM_ptj_HZZ": submit_sm_scans_ptj_HZZ,
    "SM_ptj_HZZ_asimov": submit_sm_scans_ptj_HZZ_asimov,
    "SM_ptj_HttBoost": submit_sm_scans_ptj_HttBoost,
    "SM_ptj_HttBoost_asimov": submit_sm_scans_ptj_HttBoost_asimov,
    "SM_ptj_HggHZZHttBoost": submit_sm_scans_ptj_HggHZZHttBoost,
    "SM_ptj_HggHZZHttBoost_statonly": submit_sm_scans_ptj_HggHZZHttBoost_statonly,
    "SM_ptj_HggHZZHttBoost_asimov": submit_sm_scans_ptj_HggHZZHttBoost_asimov,
    "SM_ptj_HggHZZHttBoost_asimov_statonly": submit_sm_scans_ptj_HggHZZHttBoost_asimov_statonly,
    "SM_ptj_FinalComb": submit_sm_scans_ptj_FinalComb,
    "SM_ptj_FinalComb_statonly": submit_sm_scans_ptj_FinalComb_statonly,
    "SM_ptj_FinalComb_asimov": submit_sm_scans_ptj_FinalComb_asimov,
    "SM_ptj_FinalComb_asimov_statonly": submit_sm_scans_ptj_FinalComb_asimov_statonly,
    "SM_mjj_Hgg": submit_sm_scans_mjj_Hgg,
    "SM_mjj_Hgg_asimov": submit_sm_scans_mjj_Hgg_asimov,
    "SM_mjj_HZZ": submit_sm_scans_mjj_HZZ,
    "SM_mjj_HZZ_asimov": submit_sm_scans_mjj_HZZ_asimov,
    "SM_mjj_HggHZZ": submit_sm_scans_mjj_HggHZZ,
    "SM_mjj_HggHZZ_statonly": submit_sm_scans_mjj_HggHZZ_statonly,
    "SM_mjj_HggHZZ_asimov": submit_sm_scans_mjj_HggHZZ_asimov,
    "SM_mjj_HggHZZ_asimov_statonly": submit_sm_scans_mjj_HggHZZ_asimov_statonly,
    "SM_detajj_Hgg": submit_sm_scans_detajj_Hgg,
    "SM_detajj_Hgg_asimov": submit_sm_scans_detajj_Hgg_asimov,
    "SM_detajj_HZZ": submit_sm_scans_detajj_HZZ,
    "SM_detajj_HZZ_asimov": submit_sm_scans_detajj_HZZ_asimov,
    "SM_detajj_HggHZZ": submit_sm_scans_detajj_HggHZZ,
    "SM_detajj_HggHZZ_statonly": submit_sm_scans_detajj_HggHZZ_statonly,
    "SM_detajj_HggHZZ_asimov": submit_sm_scans_detajj_HggHZZ_asimov,
    "SM_detajj_HggHZZ_asimov_statonly": submit_sm_scans_detajj_HggHZZ_asimov_statonly,
    "SM_taucj_Hgg": submit_sm_scans_taucj_Hgg,
    "SM_taucj_Hgg_asimov": submit_sm_scans_taucj_Hgg_asimov,
    "SM_taucj_HZZ": submit_sm_scans_taucj_HZZ,
    "SM_taucj_HZZ_asimov": submit_sm_scans_taucj_HZZ_asimov,
    "SM_taucj_HggHZZ": submit_sm_scans_taucj_HggHZZ,
    "SM_taucj_HggHZZ_statonly": submit_sm_scans_taucj_HggHZZ_statonly,
    "SM_taucj_HggHZZ_asimov": submit_sm_scans_taucj_HggHZZ_asimov,
    "SM_taucj_HggHZZ_asimov_statonly": submit_sm_scans_taucj_HggHZZ_asimov_statonly,
}

"""Note:
This is horrible and I hate having another class definition here instad of in tasks.py.
However, feeding a luigi.ListParameter with a list of luigi.Task objects is not possible,
as it raises the problem described here:
https://stackoverflow.com/questions/44379387/json-serialization-error-when-creating-a-luigi-task-graph

The solution is to somehow have instances of CombineCards, CreateSMWorkspace and SubmitSMScans available
before the PlotSMCrossSection class is defined. This is why we have to define them here.
"""


class PlotSMCrossSection(BaseNotifierClass):
    categories = luigi.ListParameter(default=[])
    singles = luigi.ListParameter(default=[])
    systematic_bands = luigi.OptionalParameter(default=None)
    allow_extrapolation = luigi.BoolParameter(default=False)
    submit_sm_scans = luigi.ListParameter()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.observable = submit_instances[self.submit_sm_scans[0]].observable
        self.input_dir = "{}/outputs/SM_scans/{}".format(root_dir, self.observable)
        self.output_dir = "{}/outputs/SM_plots".format(root_dir)
        self.metadata_dir = "{}/DifferentialCombinationRun2/metadata/xs_POIs/SM".format(root_dir)
        self.config_file = "{}/DifferentialCombinationRun2/metadata/xs_POIs/SM/{}/plot_config.yml".format(
            root_dir,
            self.observable,
        )

    def requires(self):
        required_tasks = []
        for submit_sm_scan in self.submit_sm_scans:
            required_tasks.append(submit_instances[submit_sm_scan])
        return required_tasks

    def run(self):
        os.environ["KRB5CCNAME"] = "/t3home/gallim/krb5cc_722"
        commands = [
            "kinit -R",
            "eosfusebind -g krb5 $HOME/krb5cc_$UID",
            "plot_xs_scans.py --observable {} --input-dir {} --metadata-dir {} --output-dir {} --config-file {}".format(
                self.observable,
                self.input_dir,
                self.metadata_dir,
                self.output_dir,
                self.config_file,
            )
        ]
        commands[2] += " --categories {}".format(" ".join(self.categories)) if self.categories else ""
        commands[2] += " --singles {}".format(" ".join(self.singles)) if self.singles else ""
        commands[2] += " --systematic-bands {}".format(self.systematic_bands) if self.systematic_bands is not None else ""
        commands[2] += " --allow-extrapolation" if self.allow_extrapolation else ""

        run_list_of_commands(commands)
        self.send_notification_complete()


plot_sm_cross_section_pt_Hgg = PlotSMCrossSection(
    categories=["Hgg"],
    submit_sm_scans=["SM_pt_Hgg"],
)

plot_sm_cross_section_pt_HWW = PlotSMCrossSection(
    categories=["HWW"],
    submit_sm_scans=["SM_pt_HWW"],
)

plot_sm_cross_section_pt_Htt = PlotSMCrossSection(
    singles=["Htt"],
    submit_sm_scans=["SM_pt_Htt"],
)

plot_sm_cross_section_pt_HbbVBF = PlotSMCrossSection(
    singles=["HbbVBF"],
    submit_sm_scans=["SM_pt_HbbVBF"],
)

plot_sm_cross_section_pt_HttBoost = PlotSMCrossSection(
    singles=["HttBoost"],
    submit_sm_scans=["SM_pt_HttBoost"],
)

plot_sm_cross_section_pt_HggHZZ = PlotSMCrossSection(
    categories=["HggHZZ", "Hgg", "HZZ"],
    submit_sm_scans=["SM_pt_HggHZZ", "SM_pt_Hgg", "SM_pt_HZZ"],
)

plot_sm_cross_section_pt_HggHZZHWWHttHbbVBFHttBoost_asimov_alone = PlotSMCrossSection(
    categories=["HggHZZHWWHttHbbVBFHttBoost"],
    systematic_bands="HggHZZHWWHttHbbVBFHttBoost",
    submit_sm_scans=[
        "SM_pt_HggHZZHWWHttHbbVBFHttBoost_asimov",
        "SM_pt_HggHZZHWWHttHbbVBFHttBoost_asimov_statonly",
    ],
)

plot_sm_cross_section_pt_HggHZZHWWHttHbbVBFHttBoost_asimov = PlotSMCrossSection(
    categories=["HggHZZHWWHttHbbVBFHttBoost", "Hgg", "HZZ", "HWW"],
    singles=["Htt", "HbbVBF", "HttBoost"],
    systematic_bands="HggHZZHWWHttHbbVBFHttBoost",
    submit_sm_scans=[
        "SM_pt_HggHZZHWWHttHbbVBFHttBoost_asimov",
        "SM_pt_HggHZZHWWHttHbbVBFHttBoost_asimov_statonly",
        "SM_pt_Hgg_asimov",
        "SM_pt_HZZ_asimov",
        "SM_pt_HWW_asimov",
        "SM_pt_Htt_asimov",
        "SM_pt_HbbVBF_asimov",
        "SM_pt_HttBoost_asimov",
    ],
)

plot_sm_cross_section_pt_FinalComb_alone = PlotSMCrossSection(
    categories=["FinalComb"],
    systematic_bands="FinalComb",
    submit_sm_scans=[
        "SM_pt_FinalComb",
        "SM_pt_FinalComb_statonly",
    ],
)

plot_sm_cross_section_pt_FinalComb = PlotSMCrossSection(
    categories=["FinalComb", "Hgg", "HZZ", "HWW"],
    singles=["Htt", "HbbVBF", "HttBoost"],
    systematic_bands="FinalComb",
    submit_sm_scans=[
        "SM_pt_FinalComb",
        "SM_pt_FinalComb_statonly",
        "SM_pt_Hgg",
        "SM_pt_HZZ",
        "SM_pt_HWW",
        "SM_pt_Htt",
        "SM_pt_HbbVBF",
        "SM_pt_HttBoost",
    ],
)

plot_sm_cross_section_pt_FinalComb_asimov_alone = PlotSMCrossSection(
    categories=["FinalComb"],
    systematic_bands="FinalComb",
    submit_sm_scans=[
        "SM_pt_FinalComb_asimov",
        "SM_pt_FinalComb_asimov_statonly",
    ],
)

plot_sm_cross_section_pt_FinalComb_asimov = PlotSMCrossSection(
    categories=["FinalComb", "Hgg", "HZZ", "HWW"],
    singles=["Htt", "HbbVBF", "HttBoost"],
    systematic_bands="FinalComb",
    submit_sm_scans=[
        "SM_pt_FinalComb_asimov",
        "SM_pt_FinalComb_asimov_statonly",
        "SM_pt_Hgg_asimov",
        "SM_pt_HZZ_asimov",
        "SM_pt_HWW_asimov",
        "SM_pt_Htt_asimov",
        "SM_pt_HbbVBF_asimov",
        "SM_pt_HttBoost_asimov",
    ],
)

plot_sm_cross_section_Njets_Hgg = PlotSMCrossSection(
    categories=["Hgg"],
    submit_sm_scans=["SM_Njets_Hgg"],
)

plot_sm_cross_section_Njets_HZZ = PlotSMCrossSection(
    categories=["HZZ"],
    allow_extrapolation=True,
    submit_sm_scans=["SM_Njets_HZZ"],
)

plot_sm_cross_section_Njets_HWW = PlotSMCrossSection(
    categories=["HWW"],
    submit_sm_scans=["SM_Njets_HWW"],
)

plot_sm_cross_section_Njets_Htt = PlotSMCrossSection(
    singles=["Htt"],
    submit_sm_scans=["SM_Njets_Htt"],
)

plot_sm_cross_section_Njets_HggHZZHWWHtt = PlotSMCrossSection(
    categories=["HggHZZHWWHtt", "Hgg", "HZZ", "HWW"],
    singles=["Htt"],
    systematic_bands="HggHZZHWWHtt",
    allow_extrapolation=True,
    submit_sm_scans=["SM_Njets_HggHZZHWWHtt", "SM_Njets_HggHZZHWWHtt_statonly", "SM_Njets_Hgg", "SM_Njets_HZZ", "SM_Njets_HWW", "SM_Njets_Htt"],
)

plot_sm_cross_section_Njets_HggHZZHWWHtt_asimov = PlotSMCrossSection(
    categories=["HggHZZHWWHtt", "Hgg", "HZZ", "HWW"],
    singles=["Htt"],
    systematic_bands="HggHZZHWWHtt",
    allow_extrapolation=True,
    submit_sm_scans=[
        "SM_Njets_HggHZZHWWHtt_asimov",
        "SM_Njets_HggHZZHWWHtt_asimov_statonly",
        "SM_Njets_Hgg_asimov",
        "SM_Njets_HZZ_asimov",
        "SM_Njets_HWW_asimov",
        "SM_Njets_Htt_asimov",
    ],
)

plot_sm_cross_section_Njets_HggHZZHWWHtt_asimov_alone = PlotSMCrossSection(
    categories=["HggHZZHWWHtt"],
    systematic_bands="HggHZZHWWHtt",
    allow_extrapolation=True,
    submit_sm_scans=[
        "SM_Njets_HggHZZHWWHtt_asimov",
        "SM_Njets_HggHZZHWWHtt_asimov_statonly",
    ],
)

plot_sm_cross_section_yH_HggHZZ = PlotSMCrossSection(
    categories=["HggHZZ", "Hgg", "HZZ"],
    systematic_bands="HggHZZ",
    submit_sm_scans=["SM_yH_HggHZZ", "SM_yH_HggHZZ_statonly", "SM_yH_Hgg", "SM_yH_HZZ"],
)

plot_sm_cross_section_yH_HggHZZ_asimov = PlotSMCrossSection(
    categories=["HggHZZ", "Hgg", "HZZ"],
    systematic_bands="HggHZZ",
    submit_sm_scans=["SM_yH_HggHZZ_asimov", "SM_yH_HggHZZ_asimov_statonly", "SM_yH_Hgg_asimov", "SM_yH_HZZ_asimov"],
)

plot_sm_cross_section_yH_HggHZZ_asimov_alone = PlotSMCrossSection(
    categories=["HggHZZ"],
    systematic_bands="HggHZZ",
    submit_sm_scans=["SM_yH_HggHZZ_asimov", "SM_yH_HggHZZ_asimov_statonly"],
)

plot_sm_cross_section_ptj_HggHZZHttBoost = PlotSMCrossSection(
    categories=["HggHZZHttBoost", "Hgg", "HZZ"],
    singles=["HttBoost"],
    systematic_bands="HggHZZHttBoost",
    submit_sm_scans=["SM_ptj_HggHZZHttBoost", "SM_ptj_HggHZZHttBoost_statonly", "SM_ptj_Hgg", "SM_ptj_HZZ", "SM_ptj_HttBoost"],
)

plot_sm_cross_section_ptj_HggHZZHttBoost_asimov = PlotSMCrossSection(
    categories=["HggHZZHttBoost", "Hgg", "HZZ"],
    singles=["HttBoost"],
    systematic_bands="HggHZZHttBoost",
    submit_sm_scans=[
        "SM_ptj_HggHZZHttBoost_asimov",
        "SM_ptj_HggHZZHttBoost_asimov_statonly",
        "SM_ptj_Hgg_asimov",
        "SM_ptj_HZZ_asimov",
        "SM_ptj_HttBoost_asimov",
    ],
)

plot_sm_cross_section_ptj_HggHZZHttBoost_asimov_alone = PlotSMCrossSection(
    categories=["HggHZZHttBoost"],
    systematic_bands="HggHZZHttBoost",
    submit_sm_scans=[
        "SM_ptj_HggHZZHttBoost_asimov",
        "SM_ptj_HggHZZHttBoost_asimov_statonly",
    ],
)

plot_sm_cross_section_ptj_FinalComb = PlotSMCrossSection(
    categories=["FinalComb", "Hgg", "HZZ"],
    singles=["HttBoost"],
    systematic_bands="FinalComb",
    submit_sm_scans=[
        "SM_ptj_FinalComb",
        "SM_ptj_FinalComb_statonly",
        "SM_ptj_Hgg",
        "SM_ptj_HZZ",
        "SM_ptj_HttBoost",
    ],
)

plot_sm_cross_section_ptj_FinalComb_asimov = PlotSMCrossSection(
    categories=["FinalComb", "Hgg", "HZZ"],
    singles=["HttBoost"],
    systematic_bands="FinalComb",
    submit_sm_scans=[
        "SM_ptj_FinalComb_asimov",
        "SM_ptj_FinalComb_asimov_statonly",
        "SM_ptj_Hgg_asimov",
        "SM_ptj_HZZ_asimov",
        "SM_ptj_HttBoost_asimov",
    ],
)

plot_sm_cross_section_ptj_FinalComb_asimov_alone = PlotSMCrossSection(
    categories=["FinalComb"],
    systematic_bands="FinalComb",
    submit_sm_scans=[
        "SM_ptj_FinalComb_asimov",
        "SM_ptj_FinalComb_asimov_statonly",
    ],
)

plot_sm_cross_section_mjj_HggHZZ = PlotSMCrossSection(
    categories=["HggHZZ", "Hgg", "HZZ"],
    systematic_bands="HggHZZ",
    submit_sm_scans=["SM_mjj_HggHZZ", "SM_mjj_HggHZZ_statonly", "SM_mjj_Hgg", "SM_mjj_HZZ"],
)

plot_sm_cross_section_mjj_HggHZZ_asimov = PlotSMCrossSection(
    categories=["HggHZZ", "Hgg", "HZZ"],
    systematic_bands="HggHZZ",
    submit_sm_scans=["SM_mjj_HggHZZ_asimov", "SM_mjj_HggHZZ_asimov_statonly", "SM_mjj_Hgg_asimov", "SM_mjj_HZZ_asimov"],
)

plot_sm_cross_section_mjj_HggHZZ_asimov_alone = PlotSMCrossSection(
    categories=["HggHZZ"],
    systematic_bands="HggHZZ",
    submit_sm_scans=["SM_mjj_HggHZZ_asimov", "SM_mjj_HggHZZ_asimov_statonly"],
)

plot_sm_cross_section_detajj_HggHZZ = PlotSMCrossSection(
    categories=["HggHZZ", "Hgg", "HZZ"],
    systematic_bands="HggHZZ",
    submit_sm_scans=["SM_detajj_HggHZZ", "SM_detajj_HggHZZ_statonly", "SM_detajj_Hgg", "SM_detajj_HZZ"],
)

plot_sm_cross_section_detajj_HggHZZ_asimov = PlotSMCrossSection(
    categories=["HggHZZ", "Hgg", "HZZ"],
    systematic_bands="HggHZZ",
    submit_sm_scans=["SM_detajj_HggHZZ_asimov", "SM_detajj_HggHZZ_asimov_statonly", "SM_detajj_Hgg_asimov", "SM_detajj_HZZ_asimov"],
)

plot_sm_cross_section_detajj_HggHZZ_asimov_alone = PlotSMCrossSection(
    categories=["HggHZZ"],
    systematic_bands="HggHZZ",
    submit_sm_scans=["SM_detajj_HggHZZ_asimov", "SM_detajj_HggHZZ_asimov_statonly"],
)

plot_sm_cross_section_taucj_HggHZZ = PlotSMCrossSection(
    categories=["HggHZZ", "Hgg", "HZZ"],
    systematic_bands="HggHZZ",
    submit_sm_scans=["SM_taucj_HggHZZ", "SM_taucj_HggHZZ_statonly", "SM_taucj_Hgg", "SM_taucj_HZZ"],
)

plot_sm_cross_section_taucj_HggHZZ_asimov = PlotSMCrossSection(
    categories=["HggHZZ", "Hgg", "HZZ"],
    systematic_bands="HggHZZ",
    submit_sm_scans=["SM_taucj_HggHZZ_asimov", "SM_taucj_HggHZZ_asimov_statonly", "SM_taucj_Hgg_asimov", "SM_taucj_HZZ_asimov"],
)

plot_sm_cross_section_taucj_HggHZZ_asimov_alone = PlotSMCrossSection(
    categories=["HggHZZ"],
    systematic_bands="HggHZZ",
    submit_sm_scans=["SM_taucj_HggHZZ_asimov", "SM_taucj_HggHZZ_asimov_statonly"],
)

"""
kappa
"""
combine_cards_yukawa_HggHZZHtt = CombineCards(
    channels=[
        "hgg=DifferentialCombinationRun2/Analyses/hig-19-016-noprune/outdir_differential_Pt/TK_Yukawa_out.txt",
        "hzz=DifferentialCombinationRun2/Analyses/Test/Yukawa_hzz_pth_ggH_Sep04_all_xHNuisPar.txt",
        "htt=DifferentialCombinationRun2/Analyses/hig-20-015/HiggsPt/HTT_Run2FinalCard_HiggsPt_NoReg_swapOOA_xHNuisPar.txt",
    ],
    output_card_name="CombinedCards/TK/Yukawa_HggHZZHtt.txt",
    extra_options=" --xc=htt_PTH_120_200* --xc=htt_PTH_200_350* --xc=htt_PTH_350_450* --xc=htt_PTH_GT350* --xc=htt_PTH_GT450*",
    replace_mass=False
)

combine_cards_top_HggHZZHttHttBoostHbbVBF = CombineCards(
    channels=[
        "hgg=DifferentialCombinationRun2/Analyses/hig-19-016-noprune/outdir_differential_Pt/TK_Top_out.txt",
        "hzz=DifferentialCombinationRun2/Analyses/Test/hzz_pth_ggH_Sep04_all.txt",
        "htt=DifferentialCombinationRun2/Analyses/hig-20-015/HiggsPt/HTT_Run2FinalCard_HiggsPt_NoReg_swapOOA_xHNuisPar.txt",
        "httboost=DifferentialCombinationRun2/Analyses/hig-21-017/BoostedHTT_DiffXS_HiggsPt_NoOverLap_New/Diff_V7_FreshRun_hpt_NoOverLap_rename/all_swapOOA.txt",
        "hbbvbf=DifferentialCombinationRun2/Analyses/hig-21-020/signal-strength/testModel/model_combined_withpaths_noVBF.txt",
    ],
    output_card_name="CombinedCards/TK/Top_HggHZZHttHttBoostHbbVBF.txt",
    extra_options=" --xc=hzz_hzz_PTH_GT600*",
    replace_mass=True
)

create_kappa_workspace_YukawaConstrained_HggHZZHtt = CreateKappaWorkspace(
    model="YukawaConstrained",
    category="HggHZZHtt",
    combine_cards=combine_cards_yukawa_HggHZZHtt,
)

create_kappa_workspace_YukawaFloat_HggHZZHtt = CreateKappaWorkspace(
    model="YukawaFloat",
    category="HggHZZHtt",
    combine_cards=combine_cards_yukawa_HggHZZHtt,
)

create_kappa_workspace_TopCgKtConstrained_HggHZZHttHttBoostHbbVBF = CreateKappaWorkspace(
    model="TopCgKtConstrained",
    category="HggHZZHttHttBoostHbbVBF",
    combine_cards=combine_cards_top_HggHZZHttHttBoostHbbVBF,
)

create_kappa_workspace_TopCgKtFloat_HggHZZHttHttBoostHbbVBF = CreateKappaWorkspace(
    model="TopCgKtFloat",
    category="HggHZZHttHttBoostHbbVBF",
    combine_cards=combine_cards_top_HggHZZHttHttBoostHbbVBF,
)

create_kappa_workspace_TopKbKtConstrained_HggHZZHttHttBoostHbbVBF = CreateKappaWorkspace(
    model="TopKbKtConstrained",
    category="HggHZZHttHttBoostHbbVBF",
    combine_cards=combine_cards_top_HggHZZHttHttBoostHbbVBF,
)

create_kappa_workspace_TopKbKtFloat_HggHZZHttHttBoostHbbVBF = CreateKappaWorkspace(
    model="TopKbKtFloat",
    category="HggHZZHttHttBoostHbbVBF",
    combine_cards=combine_cards_top_HggHZZHttHttBoostHbbVBF,
)

submit_kappa_scan_YukawaConstrained_HggHZZHtt_asimov = SubmitKappaScans(
    category="HggHZZHtt_asimov",
    create_kappa_workspace=create_kappa_workspace_YukawaConstrained_HggHZZHtt,
)

submit_kappa_scan_YukawaConstrained_HggHZZHtt = SubmitKappaScans(
    category="HggHZZHtt",
    create_kappa_workspace=create_kappa_workspace_YukawaConstrained_HggHZZHtt,
)

submit_kappa_scan_YukawaFloat_HggHZZHtt_asimov = SubmitKappaScans(
    category="HggHZZHtt_asimov",
    create_kappa_workspace=create_kappa_workspace_YukawaFloat_HggHZZHtt,
)

submit_kappa_scan_YukawaFloat_HggHZZHtt = SubmitKappaScans(
    category="HggHZZHtt",
    create_kappa_workspace=create_kappa_workspace_YukawaFloat_HggHZZHtt,
)

submit_kappa_scan_TopCgKtConstrained_HggHZZHttHttBoostHbbVBF_asimov = SubmitKappaScans(
    category="HggHZZHttHttBoostHbbVBF_asimov",
    create_kappa_workspace=create_kappa_workspace_TopCgKtConstrained_HggHZZHttHttBoostHbbVBF,
)

submit_kappa_scan_TopCgKtConstrained_HggHZZHttHttBoostHbbVBF = SubmitKappaScans(
    category="HggHZZHttHttBoostHbbVBF",
    create_kappa_workspace=create_kappa_workspace_TopCgKtConstrained_HggHZZHttHttBoostHbbVBF,
)

submit_kappa_scan_TopCgKtFloat_HggHZZHttHttBoostHbbVBF_asimov = SubmitKappaScans(
    category="HggHZZHttHttBoostHbbVBF_asimov",
    create_kappa_workspace=create_kappa_workspace_TopCgKtFloat_HggHZZHttHttBoostHbbVBF,
)

submit_kappa_scan_TopCgKtFloat_HggHZZHttHttBoostHbbVBF = SubmitKappaScans(
    category="HggHZZHttHttBoostHbbVBF",
    create_kappa_workspace=create_kappa_workspace_TopCgKtFloat_HggHZZHttHttBoostHbbVBF,
)

submit_kappa_scan_TopKbKtConstrained_HggHZZHttHttBoostHbbVBF_asimov = SubmitKappaScans(
    category="HggHZZHttHttBoostHbbVBF_asimov",
    create_kappa_workspace=create_kappa_workspace_TopKbKtConstrained_HggHZZHttHttBoostHbbVBF,
)

submit_kappa_scan_TopKbKtConstrained_HggHZZHttHttBoostHbbVBF = SubmitKappaScans(
    category="HggHZZHttHttBoostHbbVBF",
    create_kappa_workspace=create_kappa_workspace_TopKbKtConstrained_HggHZZHttHttBoostHbbVBF,
)

submit_kappa_scan_TopKbKtFloat_HggHZZHttHttBoostHbbVBF_asimov = SubmitKappaScans(
    category="HggHZZHttHttBoostHbbVBF_asimov",
    create_kappa_workspace=create_kappa_workspace_TopKbKtFloat_HggHZZHttHttBoostHbbVBF,
)

submit_kappa_scan_TopKbKtFloat_HggHZZHttHttBoostHbbVBF = SubmitKappaScans(
    category="HggHZZHttHttBoostHbbVBF",
    create_kappa_workspace=create_kappa_workspace_TopKbKtFloat_HggHZZHttHttBoostHbbVBF,
)

submit_instances_kappa = {
    "YukawaConstrained_HggHZZHtt_asimov": submit_kappa_scan_YukawaConstrained_HggHZZHtt_asimov,
    "YukawaConstrained_HggHZZHtt": submit_kappa_scan_YukawaConstrained_HggHZZHtt,
    "YukawaFloat_HggHZZHtt_asimov": submit_kappa_scan_YukawaFloat_HggHZZHtt_asimov,
    "YukawaFloat_HggHZZHtt": submit_kappa_scan_YukawaFloat_HggHZZHtt,
    "TopCgKtConstrained_HggHZZHttHttBoostHbbVBF_asimov": submit_kappa_scan_TopCgKtConstrained_HggHZZHttHttBoostHbbVBF_asimov,
    "TopCgKtConstrained_HggHZZHttHttBoostHbbVBF": submit_kappa_scan_TopCgKtConstrained_HggHZZHttHttBoostHbbVBF,
    "TopCgKtFloat_HggHZZHttHttBoostHbbVBF_asimov": submit_kappa_scan_TopCgKtFloat_HggHZZHttHttBoostHbbVBF_asimov,
    "TopCgKtFloat_HggHZZHttHttBoostHbbVBF": submit_kappa_scan_TopCgKtFloat_HggHZZHttHttBoostHbbVBF,
    "TopKbKtConstrained_HggHZZHttHttBoostHbbVBF_asimov": submit_kappa_scan_TopKbKtConstrained_HggHZZHttHttBoostHbbVBF_asimov,
    "TopKbKtConstrained_HggHZZHttHttBoostHbbVBF": submit_kappa_scan_TopKbKtConstrained_HggHZZHttHttBoostHbbVBF,
    "TopKbKtFloat_HggHZZHttHttBoostHbbVBF_asimov": submit_kappa_scan_TopKbKtFloat_HggHZZHttHttBoostHbbVBF_asimov,
    "TopKbKtFloat_HggHZZHttHttBoostHbbVBF": submit_kappa_scan_TopKbKtFloat_HggHZZHttHttBoostHbbVBF,
}


class PlotKappaLimits(BaseNotifierClass):
    categories = luigi.ListParameter()
    combination = luigi.Parameter()
    asimov = luigi.BoolParameter(default=True)
    submit_kappa_scans = luigi.ListParameter()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = submit_instances_kappa[self.submit_kappa_scans[0]].model
        self.input_dir = "{}/outputs/TK_scans".format(root_dir)
        self.output_dir = "{}/outputs/TK_plots/{}".format(root_dir, self.model)

    def requires(self):
        return [submit_instances_kappa[scan] for scan in self.submit_kappa_scans]

    def run(self):
        full_input_dir = os.path.join(
            self.input_dir,
            submit_instances_kappa[
                self.submit_kappa_scans[0]
            ].create_kappa_workspace.model_arg,
        )
        # create output directory if it doesn't exist
        if not os.path.exists(self.output_dir):
            print("Creating output directory: {}".format(self.output_dir))
            os.makedirs(self.output_dir)
        
        kappa_naming_conv_plot = {
            "YukawaConstrained": "yukawa_coupdep",
            "YukawaFloat": "yukawa_floatingBR",
            "TopCgKtConstrained": "top_coupdep_ctcg",
            "TopCgKtFloat": "top_floatingBR_ctcg",
            "TopKbKtConstrained": "top_coupdep_ctcb",
            "TopKbKtFloat": "top_floatingBR_ctcb",
        }
        os.environ["KRB5CCNAME"] = "/t3home/gallim/krb5cc_722"
        commands = [
            "kinit -R",
            "eosfusebind -g krb5 $HOME/krb5cc_$UID",
            "plot_TK_scans.py --input-dir {} --output-dir {} --model {} --categories {} --combination {}".format(
                full_input_dir,
                self.output_dir,
                kappa_naming_conv_plot[self.model],
                " ".join(self.categories),
                self.combination,
            )
            + (" --expected" if self.asimov else ""),
        ]
        run_list_of_commands(commands)
        self.send_notification_complete()


plot_kappa_YukawaConstrained_HggHZZHtt_asimov = PlotKappaLimits(
    categories=["HggHZZHtt"],
    combination="HggHZZHtt",
    asimov=True,
    submit_kappa_scans=["YukawaConstrained_HggHZZHtt_asimov"],
)

plot_kappa_YukawaConstrained_HggHZZHtt = PlotKappaLimits(
    categories=["HggHZZHtt"],
    combination="HggHZZHtt",
    asimov=False,
    submit_kappa_scans=["YukawaConstrained_HggHZZHtt"],
)

plot_kappa_YukawaFloat_HggHZZHtt_asimov = PlotKappaLimits(
    categories=["HggHZZHtt"],
    combination="HggHZZHtt",
    asimov=True,
    submit_kappa_scans=["YukawaFloat_HggHZZHtt_asimov"],
)

plot_kappa_YukawaFloat_HggHZZHtt = PlotKappaLimits(
    categories=["HggHZZHtt"],
    combination="HggHZZHtt",
    asimov=False,
    submit_kappa_scans=["YukawaFloat_HggHZZHtt"],
)

plot_kappa_TopCgKtConstrained_HggHZZHttHttBoostHbbVBF_asimov = PlotKappaLimits(
    categories=["HggHZZHttHttBoostHbbVBF"],
    combination="HggHZZHttHttBoostHbbVBF",
    asimov=True,
    submit_kappa_scans=["TopCgKtConstrained_HggHZZHttHttBoostHbbVBF_asimov"],
)

plot_kappa_TopCgKtConstrained_HggHZZHttHttBoostHbbVBF = PlotKappaLimits(
    categories=["HggHZZHttHttBoostHbbVBF"],
    combination="HggHZZHttHttBoostHbbVBF",
    asimov=False,
    submit_kappa_scans=["TopCgKtConstrained_HggHZZHttHttBoostHbbVBF"],
)

plot_kappa_TopCgKtFloat_HggHZZHttHttBoostHbbVBF_asimov = PlotKappaLimits(
    categories=["HggHZZHttHttBoostHbbVBF"],
    combination="HggHZZHttHttBoostHbbVBF",
    asimov=True,
    submit_kappa_scans=["TopCgKtFloat_HggHZZHttHttBoostHbbVBF_asimov"],
)

plot_kappa_TopCgKtFloat_HggHZZHttHttBoostHbbVBF = PlotKappaLimits(
    categories=["HggHZZHttHttBoostHbbVBF"],
    combination="HggHZZHttHttBoostHbbVBF",
    asimov=False,
    submit_kappa_scans=["TopCgKtFloat_HggHZZHttHttBoostHbbVBF"],
)

plot_kappa_TopKbKtConstrained_HggHZZHttHttBoostHbbVBF_asimov = PlotKappaLimits(
    categories=["HggHZZHttHttBoostHbbVBF"],
    combination="HggHZZHttHttBoostHbbVBF",
    asimov=True,
    submit_kappa_scans=["TopKbKtConstrained_HggHZZHttHttBoostHbbVBF_asimov"],
)

plot_kappa_TopKbKtConstrained_HggHZZHttHttBoostHbbVBF = PlotKappaLimits(
    categories=["HggHZZHttHttBoostHbbVBF"],
    combination="HggHZZHttHttBoostHbbVBF",
    asimov=False,
    submit_kappa_scans=["TopKbKtConstrained_HggHZZHttHttBoostHbbVBF"],
)

plot_kappa_TopKbKtFloat_HggHZZHttHttBoostHbbVBF_asimov = PlotKappaLimits(
    categories=["HggHZZHttHttBoostHbbVBF"],
    combination="HggHZZHttHttBoostHbbVBF",
    asimov=True,
    submit_kappa_scans=["TopKbKtFloat_HggHZZHttHttBoostHbbVBF_asimov"],
)

plot_kappa_TopKbKtFloat_HggHZZHttHttBoostHbbVBF = PlotKappaLimits(
    categories=["HggHZZHttHttBoostHbbVBF"],
    combination="HggHZZHttHttBoostHbbVBF",
    asimov=False,
    submit_kappa_scans=["TopKbKtFloat_HggHZZHttHttBoostHbbVBF"],
)

"""
SMEFT
"""
combine_cards_DeltaPhiJJ_HggHZZ = CombineCards(
    channels=[
        "hgg=DifferentialCombinationRun2/Analyses/hig-19-016/outdir_differential_AbsDeltaPhiJ1J2Jets4p7/Datacard_13TeV_differential_AbsDeltaPhiJ1J2Jets4p7.txt",
        "hzz=DifferentialCombinationRun2/Analyses/hig-21-009/dphijj/hzz4l_all_13TeV_xs_dphijj_bin_v3.txt",
    ],
    output_card_name="CombinedCards/DeltaPhiJJ/HggHZZ.txt",
)

create_smeft_workspace_DeltaPhiJJ_NLO_HggHZZ = CreateSMEFTWorkspace(
    datacard="{}/CombinedCards/DeltaPhiJJ/HggHZZ.txt".format(root_dir),
    model="230611AtlasDPJ",
    equations="CMS-ForDiff-230530-FullDecay",
    chan_obs="DeltaPhiJJHggHZZ",
    combine_cards=combine_cards_DeltaPhiJJ_HggHZZ,
)

submit_smeft_scans_DeltaPhiJJ_NLO_Chb_HggHZZ_asimov = SubmitSMEFTScans(
    category="asimov",
    submodel="ChbScen",
    create_smeft_workspace=create_smeft_workspace_DeltaPhiJJ_NLO_HggHZZ,
)

submit_smeft_scans_DeltaPhiJJ_NLO_Chb_HggHZZ = SubmitSMEFTScans(
    category="observed",
    submodel="ChbScen",
    create_smeft_workspace=create_smeft_workspace_DeltaPhiJJ_NLO_HggHZZ,
)

submit_smeft_scans_DeltaPhiJJ_NLO_Chw_HggHZZ_asimov = SubmitSMEFTScans(
    category="asimov",
    submodel="ChwScen",
    create_smeft_workspace=create_smeft_workspace_DeltaPhiJJ_NLO_HggHZZ,
)

submit_smeft_scans_DeltaPhiJJ_NLO_Chw_HggHZZ = SubmitSMEFTScans(
    category="observed",
    submodel="ChwScen",
    create_smeft_workspace=create_smeft_workspace_DeltaPhiJJ_NLO_HggHZZ,
)

submit_smeft_scans_DeltaPhiJJ_NLO_Chwb_HggHZZ_asimov = SubmitSMEFTScans(
    category="asimov",
    submodel="ChwbScen",
    create_smeft_workspace=create_smeft_workspace_DeltaPhiJJ_NLO_HggHZZ,
)

submit_smeft_scans_DeltaPhiJJ_NLO_Chwb_HggHZZ = SubmitSMEFTScans(
    category="observed",
    submodel="ChwbScen",
    create_smeft_workspace=create_smeft_workspace_DeltaPhiJJ_NLO_HggHZZ,
)

create_smeft_workspace_DeltaPhiJJ_LO_HggHZZ = CreateSMEFTWorkspace(
    datacard="{}/CombinedCards/DeltaPhiJJ/HggHZZ.txt".format(root_dir),
    model="230611AtlasDPJ",
    equations="CMS-ForDiffAllSMEFTsim-230530",
    chan_obs="DeltaPhiJJHggHZZ",
    combine_cards=combine_cards_DeltaPhiJJ_HggHZZ,
)

submit_smeft_scans_DeltaPhiJJ_LO_Chg_HggHZZ_asimov = SubmitSMEFTScans(
    category="asimov",
    submodel="ChgScen",
    create_smeft_workspace=create_smeft_workspace_DeltaPhiJJ_LO_HggHZZ,
)

submit_smeft_scans_DeltaPhiJJ_LO_Chg_HggHZZ = SubmitSMEFTScans(
    category="observed",
    submodel="ChgScen",
    create_smeft_workspace=create_smeft_workspace_DeltaPhiJJ_LO_HggHZZ,
)

combine_cards_smeft_pt_HggHZZHWWHttHbbVBFHttBoost = CombineCards(
    channels=[
        "hgg=DifferentialCombinationRun2/Analyses/hig-19-016/outdir_differential_Pt/Datacard_13TeV_differential_Pt.txt",
        "hzz=DifferentialCombinationRun2/Analyses/hig-21-009/pT4l/hzz4l_all_13TeV_xs_pT4l_bin_v3.txt",
        "hww=DifferentialCombinationRun2/Analyses/hig-19-002/ptH_for_differential_combination/fullmodel_unreg.txt",
        "htt=DifferentialCombinationRun2/Analyses/hig-20-015/HiggsPt/HTT_Run2FinalCard_HiggsPt_NoReg_swapOOA.txt",
        "hbbvbf=DifferentialCombinationRun2/Analyses/hig-21-020/signal-strength/testModel/model_combined_withpaths_noVBF.txt",
        "httboost=DifferentialCombinationRun2/Analyses/hig-21-017/BoostedHTT_DiffXS_HiggsPt_NoOverLap_New/Diff_V7_FreshRun_hpt_NoOverLap_rename/all_swapOOA.txt"
    ],
    output_card_name="CombinedCards/smH_PTH/HggHZZHWWHttHbbVBFHttBoost_smeft.txt",
    replace_mass=True
)

create_smeft_workspace_pt_NLO_FullComb = CreateSMEFTWorkspace(
    datacard="{}/CombinedCards/smH_PTH/HggHZZHWWHttHbbVBFHttBoost_smeft.txt".format(root_dir),
    model="220926Atlas",
    equations="CMS-ForDiff-230530-FullDecay",
    chan_obs="PtFullComb",
    combine_cards=combine_cards_smeft_pt_HggHZZHWWHttHbbVBFHttBoost,
)

submit_smeft_scans_pt_FullComb_NLO_Chb_asimov = SubmitSMEFTScans(
    category="asimov",
    submodel="ChbScen",
    create_smeft_workspace=create_smeft_workspace_pt_NLO_FullComb,
)

submit_smeft_scans_pt_FullComb_NLO_Chb = SubmitSMEFTScans(
    category="observed",
    submodel="ChbScen",
    create_smeft_workspace=create_smeft_workspace_pt_NLO_FullComb,
)

submit_smeft_scans_pt_FullComb_NLO_Chw_asimov = SubmitSMEFTScans(
    category="asimov",
    submodel="ChwScen",
    create_smeft_workspace=create_smeft_workspace_pt_NLO_FullComb,
)

submit_smeft_scans_pt_FullComb_NLO_Chw = SubmitSMEFTScans(
    category="observed",
    submodel="ChwScen",
    create_smeft_workspace=create_smeft_workspace_pt_NLO_FullComb,
)

submit_smeft_scans_pt_FullComb_NLO_Chwb_asimov = SubmitSMEFTScans(
    category="asimov",
    submodel="ChwbScen",
    create_smeft_workspace=create_smeft_workspace_pt_NLO_FullComb,
)

submit_smeft_scans_pt_FullComb_NLO_Chwb = SubmitSMEFTScans(
    category="observed",
    submodel="ChwbScen",
    create_smeft_workspace=create_smeft_workspace_pt_NLO_FullComb,
)

create_smeft_workspace_pt_LO_FullComb = CreateSMEFTWorkspace(
    datacard="{}/CombinedCards/smH_PTH/HggHZZHWWHttHbbVBFHttBoost_smeft.txt".format(root_dir),
    model="220926Atlas",
    equations="CMS-ForDiffAllSMEFTsim-230530-FullDecay",
    chan_obs="PtFullComb",
    combine_cards=combine_cards_smeft_pt_HggHZZHWWHttHbbVBFHttBoost,
)

submit_smeft_scans_pt_FullComb_LO_Chg_asimov = SubmitSMEFTScans(
    category="asimov",
    submodel="ChgScen",
    create_smeft_workspace=create_smeft_workspace_pt_LO_FullComb,
)

submit_smeft_scans_pt_FullComb_LO_Chg = SubmitSMEFTScans(
    category="observed",
    submodel="ChgScen",
    create_smeft_workspace=create_smeft_workspace_pt_LO_FullComb,
)

create_smeft_workspace_pt_PCA_FullComb = CreateSMEFTWorkspace(
    datacard="{}/CombinedCards/smH_PTH/HggHZZHWWHttHbbVBFHttBoost_smeft.txt".format(root_dir),
    model="230620PruneNoCPEVPtFullCombLinearised",
    equations="CMS-ForDiff-230530_rotated230620PruneNoCPPtFullCombA",
    chan_obs="PtFullComb",
    linearised=True,
    combine_cards=combine_cards_smeft_pt_HggHZZHWWHttHbbVBFHttBoost,
)

submit_smeft_scans_pt_FullComb_PCA_asimov = SubmitSMEFTScans(
    category="asimov",
    skip_twod=True,
    create_smeft_workspace=create_smeft_workspace_pt_PCA_FullComb,
)

submit_smeft_scans_pt_FullComb_PCA_asimov_statonly = SubmitSMEFTScans(
    category="statonly_asimov",
    skip_twod=True,
    create_smeft_workspace=create_smeft_workspace_pt_PCA_FullComb,
    full_stat_task=submit_smeft_scans_pt_FullComb_PCA_asimov,
)

submit_smeft_scans_pt_FullComb_PCA = SubmitSMEFTScans(
    category="observed",
    skip_twod=True,
    create_smeft_workspace=create_smeft_workspace_pt_PCA_FullComb,
)

submit_instances_smeft = {
    "DeltaPhiJJ_NLO_Chb_HggHZZ_asimov": submit_smeft_scans_DeltaPhiJJ_NLO_Chb_HggHZZ_asimov,
    "DeltaPhiJJ_NLO_Chb_HggHZZ": submit_smeft_scans_DeltaPhiJJ_NLO_Chb_HggHZZ,
    "DeltaPhiJJ_NLO_Chw_HggHZZ_asimov": submit_smeft_scans_DeltaPhiJJ_NLO_Chw_HggHZZ_asimov,
    "DeltaPhiJJ_NLO_Chw_HggHZZ": submit_smeft_scans_DeltaPhiJJ_NLO_Chw_HggHZZ,
    "DeltaPhiJJ_NLO_Chwb_HggHZZ_asimov": submit_smeft_scans_DeltaPhiJJ_NLO_Chwb_HggHZZ_asimov,
    "DeltaPhiJJ_NLO_Chwb_HggHZZ": submit_smeft_scans_DeltaPhiJJ_NLO_Chwb_HggHZZ,
    "DeltaPhiJJ_LO_Chg_HggHZZ_asimov": submit_smeft_scans_DeltaPhiJJ_LO_Chg_HggHZZ_asimov,
    "DeltaPhiJJ_LO_Chg_HggHZZ": submit_smeft_scans_DeltaPhiJJ_LO_Chg_HggHZZ,
    "pt_FullComb_NLO_Chb_asimov": submit_smeft_scans_pt_FullComb_NLO_Chb_asimov,
    "pt_FullComb_NLO_Chb": submit_smeft_scans_pt_FullComb_NLO_Chb,
    "pt_FullComb_NLO_Chw_asimov": submit_smeft_scans_pt_FullComb_NLO_Chw_asimov,
    "pt_FullComb_NLO_Chw": submit_smeft_scans_pt_FullComb_NLO_Chw,
    "pt_FullComb_NLO_Chwb_asimov": submit_smeft_scans_pt_FullComb_NLO_Chwb_asimov,
    "pt_FullComb_NLO_Chwb": submit_smeft_scans_pt_FullComb_NLO_Chwb,
    "pt_FullComb_LO_Chg_asimov": submit_smeft_scans_pt_FullComb_LO_Chg_asimov,
    "pt_FullComb_LO_Chg": submit_smeft_scans_pt_FullComb_LO_Chg,
    "pt_FullComb_PCA_asimov": submit_smeft_scans_pt_FullComb_PCA_asimov,
    "pt_FullComb_PCA_asimov_statonly": submit_smeft_scans_pt_FullComb_PCA_asimov_statonly,
    "pt_FullComb_PCA": submit_smeft_scans_pt_FullComb_PCA,
}

class PlotSMEFTScans(BaseNotifierClass):
    categories = luigi.ListParameter()
    combination = luigi.Parameter()
    how = luigi.Parameter()
    skip_twod = luigi.BoolParameter(default=False)
    force_twod_lim = luigi.BoolParameter(default=False)
    summary_plot = luigi.BoolParameter(default=False)
    submit_smeft_scans = luigi.ListParameter()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.input_dir = "{}/outputs/SMEFT_scans".format(root_dir)
        self.output_dir = "{}/outputs/SMEFT_plots".format(root_dir)
        self.model = submit_instances_smeft[self.submit_smeft_scans[0]].model
        self.submodel_config_file = submit_instances_smeft[self.submit_smeft_scans[0]].submodel_config_file
        self.cuts_file = "{}/DifferentialCombinationRun2/metadata/SMEFT/plot_config.yml".format(root_dir)

    def requires(self):
        return [submit_instances_smeft[scan] for scan in self.submit_smeft_scans]
    
    def run(self):
        os.environ["KRB5CCNAME"] = "/t3home/gallim/krb5cc_722"
        commands = [
            "kinit -R",
            "eosfusebind -g krb5 $HOME/krb5cc_$UID",
            "plot_SMEFT_scans.py --how submodel --input-dir {} --output-dir {} --model {} --submodel {} --categories {} --combination {} --config-file {}".format(
                self.input_dir,
                self.output_dir,
                self.model,
                self.submodel_config_file,
                " ".join(self.categories),
                self.combination,
                self.cuts_file,
            ) + " --skip-2d" * self.skip_twod + " --force-2D-limit" * self.force_twod_lim + " --summary-plot" * self.summary_plot,
        ]
        if self.how in ["expected", "expected-bkg"]:
            commands[2] += " --{}".format(self.how)
        run_list_of_commands(commands)
        self.send_notification_complete()

plot_smeft_DeltaPhiJJ_NLO_Chb_HggHZZ_asimov = PlotSMEFTScans(
    categories=["DeltaPhiJJHggHZZ"],
    combination="DeltaPhiJJHggHZZ",
    how="expected",
    skip_twod=False,
    submit_smeft_scans=["DeltaPhiJJ_NLO_Chb_HggHZZ_asimov"],
    force_twod_lim=True,
)

plot_smeft_DeltaPhiJJ_NLO_Chb_HggHZZ_asimovbkg = PlotSMEFTScans(
    categories=["DeltaPhiJJHggHZZ"],
    combination="DeltaPhiJJHggHZZ",
    how="expected-bkg",
    skip_twod=False,
    submit_smeft_scans=["DeltaPhiJJ_NLO_Chb_HggHZZ_asimov", "DeltaPhiJJ_NLO_Chb_HggHZZ"],
    force_twod_lim=True,
)

plot_smeft_DeltaPhiJJ_NLO_Chb_HggHZZ = PlotSMEFTScans(
    categories=["DeltaPhiJJHggHZZ"],
    combination="DeltaPhiJJHggHZZ",
    how="observed",
    skip_twod=False,
    submit_smeft_scans=["DeltaPhiJJ_NLO_Chb_HggHZZ"],
    force_twod_lim=True,
)

plot_smeft_DeltaPhiJJ_NLO_Chw_HggHZZ_asimov = PlotSMEFTScans(
    categories=["DeltaPhiJJHggHZZ"],
    combination="DeltaPhiJJHggHZZ",
    how="expected",
    skip_twod=False,
    submit_smeft_scans=["DeltaPhiJJ_NLO_Chw_HggHZZ_asimov"],
    force_twod_lim=True,
)

plot_smeft_DeltaPhiJJ_NLO_Chw_HggHZZ_asimovbkg = PlotSMEFTScans(
    categories=["DeltaPhiJJHggHZZ"],
    combination="DeltaPhiJJHggHZZ",
    how="expected-bkg",
    skip_twod=False,
    submit_smeft_scans=["DeltaPhiJJ_NLO_Chw_HggHZZ_asimov", "DeltaPhiJJ_NLO_Chw_HggHZZ"],
    force_twod_lim=True,
)

plot_smeft_DeltaPhiJJ_NLO_Chw_HggHZZ = PlotSMEFTScans(
    categories=["DeltaPhiJJHggHZZ"],
    combination="DeltaPhiJJHggHZZ",
    how="observed",
    skip_twod=False,
    submit_smeft_scans=["DeltaPhiJJ_NLO_Chw_HggHZZ"],
    force_twod_lim=True,
)

plot_smeft_DeltaPhiJJ_NLO_Chwb_HggHZZ_asimov = PlotSMEFTScans(
    categories=["DeltaPhiJJHggHZZ"],
    combination="DeltaPhiJJHggHZZ",
    how="expected",
    skip_twod=False,
    submit_smeft_scans=["DeltaPhiJJ_NLO_Chwb_HggHZZ_asimov"],
    force_twod_lim=True,
)

plot_smeft_DeltaPhiJJ_NLO_Chwb_HggHZZ_asimovbkg = PlotSMEFTScans(
    categories=["DeltaPhiJJHggHZZ"],
    combination="DeltaPhiJJHggHZZ",
    how="expected-bkg",
    skip_twod=False,
    submit_smeft_scans=["DeltaPhiJJ_NLO_Chwb_HggHZZ_asimov", "DeltaPhiJJ_NLO_Chwb_HggHZZ"],
    force_twod_lim=True,
)

plot_smeft_DeltaPhiJJ_NLO_Chwb_HggHZZ = PlotSMEFTScans(
    categories=["DeltaPhiJJHggHZZ"],
    combination="DeltaPhiJJHggHZZ",
    how="observed",
    skip_twod=False,
    submit_smeft_scans=["DeltaPhiJJ_NLO_Chwb_HggHZZ"],
    force_twod_lim=True,
)

plot_smeft_DeltaPhiJJ_LO_Chg_HggHZZ_asimov = PlotSMEFTScans(
    categories=["DeltaPhiJJHggHZZ"],
    combination="DeltaPhiJJHggHZZ",
    how="expected",
    skip_twod=False,
    submit_smeft_scans=["DeltaPhiJJ_LO_Chg_HggHZZ_asimov"],
    force_twod_lim=True,
)

plot_smeft_DeltaPhiJJ_LO_Chg_HggHZZ_asimovbkg = PlotSMEFTScans(
    categories=["DeltaPhiJJHggHZZ"],
    combination="DeltaPhiJJHggHZZ",
    how="expected-bkg",
    skip_twod=False,
    submit_smeft_scans=["DeltaPhiJJ_LO_Chg_HggHZZ_asimov", "DeltaPhiJJ_LO_Chg_HggHZZ"],
    force_twod_lim=True,
)

plot_smeft_DeltaPhiJJ_LO_Chg_HggHZZ = PlotSMEFTScans(
    categories=["DeltaPhiJJHggHZZ"],
    combination="DeltaPhiJJHggHZZ",
    how="observed",
    skip_twod=False,
    submit_smeft_scans=["DeltaPhiJJ_LO_Chg_HggHZZ"],
    force_twod_lim=True,
)

plot_smeft_pt_FullComb_NLO_Chb_asimov = PlotSMEFTScans(
    categories=["PtFullComb"],
    combination="PtFullComb",
    how="expected",
    skip_twod=False,
    submit_smeft_scans=["pt_FullComb_NLO_Chb_asimov"],
    force_twod_lim=True,
)

plot_smeft_pt_FullComb_NLO_Chb_asimovbkg = PlotSMEFTScans(
    categories=["PtFullComb"],
    combination="PtFullComb",
    how="expected-bkg",
    skip_twod=False,
    submit_smeft_scans=["pt_FullComb_NLO_Chb_asimov", "pt_FullComb_NLO_Chb"],
    force_twod_lim=True,
)

plot_smeft_pt_FullComb_NLO_Chb = PlotSMEFTScans(
    categories=["PtFullComb"],
    combination="PtFullComb",
    how="observed",
    skip_twod=False,
    submit_smeft_scans=["pt_FullComb_NLO_Chb"],
    force_twod_lim=True,
)

plot_smeft_pt_FullComb_NLO_Chw_asimov = PlotSMEFTScans(
    categories=["PtFullComb"],
    combination="PtFullComb",
    how="expected",
    skip_twod=False,
    submit_smeft_scans=["pt_FullComb_NLO_Chw_asimov"],
    force_twod_lim=True,
)

plot_smeft_pt_FullComb_NLO_Chw_asimovbkg = PlotSMEFTScans(
    categories=["PtFullComb"],
    combination="PtFullComb",
    how="expected-bkg",
    skip_twod=False,
    submit_smeft_scans=["pt_FullComb_NLO_Chw_asimov", "pt_FullComb_NLO_Chw"],
    force_twod_lim=True,
)

plot_smeft_pt_FullComb_NLO_Chw = PlotSMEFTScans(
    categories=["PtFullComb"],
    combination="PtFullComb",
    how="observed",
    skip_twod=False,
    submit_smeft_scans=["pt_FullComb_NLO_Chw"],
    force_twod_lim=True,
)

plot_smeft_pt_FullComb_NLO_Chwb_asimov = PlotSMEFTScans(
    categories=["PtFullComb"],
    combination="PtFullComb",
    how="expected",
    skip_twod=False,
    submit_smeft_scans=["pt_FullComb_NLO_Chwb_asimov"],
    force_twod_lim=True,
)

plot_smeft_pt_FullComb_NLO_Chwb_asimovbkg = PlotSMEFTScans(
    categories=["PtFullComb"],
    combination="PtFullComb",
    how="expected-bkg",
    skip_twod=False,
    submit_smeft_scans=["pt_FullComb_NLO_Chwb_asimov", "pt_FullComb_NLO_Chwb"],
    force_twod_lim=True,
)

plot_smeft_pt_FullComb_NLO_Chwb = PlotSMEFTScans(
    categories=["PtFullComb"],
    combination="PtFullComb",
    how="observed",
    skip_twod=False,
    submit_smeft_scans=["pt_FullComb_NLO_Chwb"],
    force_twod_lim=True,
)

plot_smeft_pt_FullComb_LO_Chg_asimov = PlotSMEFTScans(
    categories=["PtFullComb"],
    combination="PtFullComb",
    how="expected",
    skip_twod=False,
    submit_smeft_scans=["pt_FullComb_LO_Chg_asimov"],
    force_twod_lim=True,
)

plot_smeft_pt_FullComb_LO_Chg_asimovbkg = PlotSMEFTScans(
    categories=["PtFullComb"],
    combination="PtFullComb",
    how="expected-bkg",
    skip_twod=False,
    submit_smeft_scans=["pt_FullComb_LO_Chg_asimov", "pt_FullComb_LO_Chg"],
    force_twod_lim=True,
)

plot_smeft_pt_FullComb_LO_Chg = PlotSMEFTScans(
    categories=["PtFullComb"],
    combination="PtFullComb",
    how="observed",
    skip_twod=False,
    submit_smeft_scans=["pt_FullComb_LO_Chg"],
    force_twod_lim=True,
)

plot_smeft_pt_FullComb_PCA_asimov = PlotSMEFTScans(
    categories=["PtFullComb"],
    combination="PtFullComb",
    how="expected",
    skip_twod=True,
    submit_smeft_scans=["pt_FullComb_PCA_asimov"],
    summary_plot=True,
    force_twod_lim=False,
)

plot_smeft_pt_FullComb_PCA = PlotSMEFTScans(
    categories=["PtFullComb"],
    combination="PtFullComb",
    how="observed",
    skip_twod=True,
    submit_smeft_scans=["pt_FullComb_PCA"],
    summary_plot=True,
    force_twod_lim=False,
)

instances = {
    "SM_pt_Hgg": plot_sm_cross_section_pt_Hgg,
    "SM_pt_HWW": plot_sm_cross_section_pt_HWW,
    "SM_pt_Htt": plot_sm_cross_section_pt_Htt,
    "SM_pt_HggHZZ": plot_sm_cross_section_pt_HggHZZ,
    "SM_pt_HggHZZHWWHttHbbVBFHttBoost_asimov_alone": plot_sm_cross_section_pt_HggHZZHWWHttHbbVBFHttBoost_asimov_alone,
    "SM_pt_HggHZZHWWHttHbbVBFHttBoost_asimov": plot_sm_cross_section_pt_HggHZZHWWHttHbbVBFHttBoost_asimov,
    "SM_pt_FinalComb": plot_sm_cross_section_pt_FinalComb,
    "SM_pt_FinalComb_alone": plot_sm_cross_section_pt_FinalComb_alone,
    "SM_pt_FinalComb_asimov": plot_sm_cross_section_pt_FinalComb_asimov,
    "SM_pt_FinalComb_asimov_alone": plot_sm_cross_section_pt_FinalComb_asimov_alone,
    "SM_Njets_Hgg": plot_sm_cross_section_Njets_Hgg,
    "SM_Njets_HZZ": plot_sm_cross_section_Njets_HZZ,
    "SM_Njets_HWW": plot_sm_cross_section_Njets_HWW,
    "SM_Njets_Htt": plot_sm_cross_section_Njets_Htt,
    "SM_Njets_HggHZZHWWHtt": plot_sm_cross_section_Njets_HggHZZHWWHtt,
    "SM_Njets_HggHZZHWWHtt_asimov": plot_sm_cross_section_Njets_HggHZZHWWHtt_asimov,
    "SM_Njets_HggHZZHWWHtt_asimov_alone": plot_sm_cross_section_Njets_HggHZZHWWHtt_asimov_alone,
    "SM_yH_HggHZZ": plot_sm_cross_section_yH_HggHZZ,
    "SM_yH_HggHZZ_asimov": plot_sm_cross_section_yH_HggHZZ_asimov,
    "SM_yH_HggHZZ_asimov_alone": plot_sm_cross_section_yH_HggHZZ_asimov_alone,
    "SM_ptj_HggHZZHttBoost": plot_sm_cross_section_ptj_HggHZZHttBoost,
    "SM_ptj_HggHZZHttBoost_asimov": plot_sm_cross_section_ptj_HggHZZHttBoost_asimov, 
    "SM_ptj_HggHZZHttBoost_asimov_alone": plot_sm_cross_section_ptj_HggHZZHttBoost_asimov_alone, 
    "SM_ptj_FinalComb": plot_sm_cross_section_ptj_FinalComb,
    "SM_ptj_FinalComb_asimov": plot_sm_cross_section_ptj_FinalComb_asimov,
    "SM_ptj_FinalComb_asimov_alone": plot_sm_cross_section_ptj_FinalComb_asimov_alone,
    "SM_mjj_HggHZZ": plot_sm_cross_section_mjj_HggHZZ,
    "SM_mjj_HggHZZ_asimov": plot_sm_cross_section_mjj_HggHZZ_asimov,
    "SM_mjj_HggHZZ_asimov_alone": plot_sm_cross_section_mjj_HggHZZ_asimov_alone,
    "SM_detajj_HggHZZ": plot_sm_cross_section_detajj_HggHZZ,
    "SM_detajj_HggHZZ_asimov": plot_sm_cross_section_detajj_HggHZZ_asimov,
    "SM_detajj_HggHZZ_asimov_alone": plot_sm_cross_section_detajj_HggHZZ_asimov_alone,
    "SM_taucj_HggHZZ": plot_sm_cross_section_taucj_HggHZZ,
    "SM_taucj_HggHZZ_asimov": plot_sm_cross_section_taucj_HggHZZ_asimov,
    "SM_taucj_HggHZZ_asimov_alone": plot_sm_cross_section_taucj_HggHZZ_asimov_alone,
    "kappa_YukawaConstrained_HggHZZHtt_asimov": plot_kappa_YukawaConstrained_HggHZZHtt_asimov,
    "kappa_YukawaConstrained_HggHZZHtt": plot_kappa_YukawaConstrained_HggHZZHtt,
    "kappa_YukawaFloat_HggHZZHtt_asimov": plot_kappa_YukawaFloat_HggHZZHtt_asimov,
    "kappa_YukawaFloat_HggHZZHtt": plot_kappa_YukawaFloat_HggHZZHtt,
    "kappa_TopCgKtConstrained_HggHZZHttHttBoostHbbVBF_asimov": plot_kappa_TopCgKtConstrained_HggHZZHttHttBoostHbbVBF_asimov,
    "kappa_TopCgKtConstrained_HggHZZHttHttBoostHbbVBF": plot_kappa_TopCgKtConstrained_HggHZZHttHttBoostHbbVBF,
    "kappa_TopCgKtFloat_HggHZZHttHttBoostHbbVBF_asimov": plot_kappa_TopCgKtFloat_HggHZZHttHttBoostHbbVBF_asimov,
    "kappa_TopCgKtFloat_HggHZZHttHttBoostHbbVBF": plot_kappa_TopCgKtFloat_HggHZZHttHttBoostHbbVBF,
    "kappa_TopKbKtConstrained_HggHZZHttHttBoostHbbVBF_asimov": plot_kappa_TopKbKtConstrained_HggHZZHttHttBoostHbbVBF_asimov,
    "kappa_TopKbKtConstrained_HggHZZHttHttBoostHbbVBF": plot_kappa_TopKbKtConstrained_HggHZZHttHttBoostHbbVBF,
    "kappa_TopKbKtFloat_HggHZZHttHttBoostHbbVBF_asimov": plot_kappa_TopKbKtFloat_HggHZZHttHttBoostHbbVBF_asimov,
    "kappa_TopKbKtFloat_HggHZZHttHttBoostHbbVBF": plot_kappa_TopKbKtFloat_HggHZZHttHttBoostHbbVBF,
    "smeft_DeltaPhiJJ_NLO_Chb_HggHZZ": plot_smeft_DeltaPhiJJ_NLO_Chb_HggHZZ,
    "smeft_DeltaPhiJJ_NLO_Chb_HggHZZ_asimov": plot_smeft_DeltaPhiJJ_NLO_Chb_HggHZZ_asimov,
    "smeft_DeltaPhiJJ_NLO_Chb_HggHZZ_asimovbkg": plot_smeft_DeltaPhiJJ_NLO_Chb_HggHZZ_asimovbkg,
    "smeft_DeltaPhiJJ_NLO_Chw_HggHZZ": plot_smeft_DeltaPhiJJ_NLO_Chw_HggHZZ,
    "smeft_DeltaPhiJJ_NLO_Chw_HggHZZ_asimov": plot_smeft_DeltaPhiJJ_NLO_Chw_HggHZZ_asimov,
    "smeft_DeltaPhiJJ_NLO_Chw_HggHZZ_asimovbkg": plot_smeft_DeltaPhiJJ_NLO_Chw_HggHZZ_asimovbkg,
    "smeft_DeltaPhiJJ_NLO_Chwb_HggHZZ": plot_smeft_DeltaPhiJJ_NLO_Chwb_HggHZZ,
    "smeft_DeltaPhiJJ_NLO_Chwb_HggHZZ_asimov": plot_smeft_DeltaPhiJJ_NLO_Chwb_HggHZZ_asimov,
    "smeft_DeltaPhiJJ_NLO_Chwb_HggHZZ_asimovbkg": plot_smeft_DeltaPhiJJ_NLO_Chwb_HggHZZ_asimovbkg,
    "smeft_DeltaPhiJJ_LO_Chg_HggHZZ": plot_smeft_DeltaPhiJJ_LO_Chg_HggHZZ,
    "smeft_DeltaPhiJJ_LO_Chg_HggHZZ_asimov": plot_smeft_DeltaPhiJJ_LO_Chg_HggHZZ_asimov,
    "smeft_DeltaPhiJJ_LO_Chg_HggHZZ_asimovbkg": plot_smeft_DeltaPhiJJ_LO_Chg_HggHZZ_asimovbkg,
    "smeft_pt_FullComb_NLO_Chb": plot_smeft_pt_FullComb_NLO_Chb,
    "smeft_pt_FullComb_NLO_Chb_asimov": plot_smeft_pt_FullComb_NLO_Chb_asimov,
    "smeft_pt_FullComb_NLO_Chb_asimovbkg": plot_smeft_pt_FullComb_NLO_Chb_asimovbkg,
    "smeft_pt_FullComb_NLO_Chw": plot_smeft_pt_FullComb_NLO_Chw,
    "smeft_pt_FullComb_NLO_Chw_asimov": plot_smeft_pt_FullComb_NLO_Chw_asimov,
    "smeft_pt_FullComb_NLO_Chw_asimovbkg": plot_smeft_pt_FullComb_NLO_Chw_asimovbkg,
    "smeft_pt_FullComb_NLO_Chwb": plot_smeft_pt_FullComb_NLO_Chwb,
    "smeft_pt_FullComb_NLO_Chwb_asimov": plot_smeft_pt_FullComb_NLO_Chwb_asimov,
    "smeft_pt_FullComb_NLO_Chwb_asimovbkg": plot_smeft_pt_FullComb_NLO_Chwb_asimovbkg,
    "smeft_pt_FullComb_LO_Chg": plot_smeft_pt_FullComb_LO_Chg,
    "smeft_pt_FullComb_LO_Chg_asimov": plot_smeft_pt_FullComb_LO_Chg_asimov,
    "smeft_pt_FullComb_LO_Chg_asimovbkg": plot_smeft_pt_FullComb_LO_Chg_asimovbkg,
    "smeft_pt_FullComb_PCA_asimov": plot_smeft_pt_FullComb_PCA_asimov,
    "smeft_pt_FullComb_PCA": plot_smeft_pt_FullComb_PCA,
}
