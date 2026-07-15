"""Module for exaSPIM Smartsheet models."""

from typing import List

from pydantic import BaseModel, ConfigDict, Field


class MouseTracker(BaseModel):
    """Mouse Tracker Sheet Information."""

    model_config = ConfigDict(coerce_numbers_to_str=True)
    num: int = Field(..., title="#", validation_alias="3714301747482500")
    ex_m_processing_status: str | None = Field(
        default=None,
        title="ExM processing status?",
        validation_alias="3659183871184772",
    )
    status: str | None = Field(
        default=None, title="Status", validation_alias="1458059328049028"
    )
    mouse_id: str | None = Field(
        default=None, title="Mouse ID", validation_alias="1462501933797252"
    )
    sample_name: str | None = Field(
        default=None, title="Sample Name", validation_alias="6853034603663236"
    )
    workflow: str | None = Field(
        default=None, title="Workflow", validation_alias="8039677411938180"
    )
    project_description: str | None = Field(
        default=None,
        title="Project Description ",
        validation_alias="1484022992555908",
    )
    expression_time_days: str | None = Field(
        default=None,
        title="Expression time (days)",
        validation_alias="144086045249412",
    )
    pedigree: str | None = Field(
        default=None, title="Pedigree", validation_alias="5966101561167748"
    )
    sex: str | None = Field(
        default=None, title="Sex", validation_alias="8217901374852996"
    )
    dob: str | None = Field(
        default=None, title="DOB", validation_alias="899551980375940"
    )
    stx_injection_requested: str | None = Field(
        default=None,
        title="Stx Injection Requested?",
        validation_alias="5403151607746436",
    )
    ro_injection_requested: str | None = Field(
        default=None,
        title="RO Injection Requested?",
        validation_alias="2782795786047364",
    )
    perfusion_requested: str | None = Field(
        default=None,
        title="Perfusion Requested?",
        validation_alias="158378064039812",
    )
    inj_details_tam_dose: str | None = Field(
        default=None,
        title="Inj Details/TAM dose",
        validation_alias="2957816813801348",
    )
    tam_dosing_last_day: str | None = Field(
        default=None,
        title="TAM dosing (last day)",
        validation_alias="5565393041051524",
    )
    label: str | None = Field(
        default=None, title="Label", validation_alias="3916359265111940"
    )
    virus_mix_ro: str | None = Field(
        default=None, title="Virus Mix RO", validation_alias="6923460195340164"
    )
    virus_mix_total_volume_injected_ro_ul: str | None = Field(
        default=None,
        title="Virus Mix Total Volume injected RO (uL)",
        validation_alias="4698119271829380",
    )
    virus_mix_vehicle_ro: str | None = Field(
        default=None,
        title="Virus Mix Vehicle RO",
        validation_alias="404781915918212",
    )
    virus1_injection_date: str | None = Field(
        default=None,
        title="Virus1 Injection Date",
        validation_alias="8180414900293508",
    )
    virus1_age_of_injection: str | None = Field(
        default=None,
        title="Virus1 Age of Injection",
        validation_alias="862065505816452",
    )
    virus1_injection_type: str | None = Field(
        default=None,
        title="Virus1 Injection Type",
        validation_alias="1061793413681028",
    )
    virus1: str | None = Field(
        default=None, title="Virus1", validation_alias="5365665133186948"
    )
    ai_p_num: str | None = Field(
        default=None, title="AiP#", validation_alias="5618574067453828"
    )
    virus1_id: str | None = Field(
        default=None, title="Virus1 ID", validation_alias="3113865319501700"
    )
    virus1_stock_titer_gc_ml: str | None = Field(
        default=None,
        title="Virus1 Stock Titer (GC/mL)",
        validation_alias="7617464946872196",
    )
    working_titer_gc_ml: str | None = Field(
        default=None,
        title="Working Titer (GC/mL)",
        validation_alias="4275549066973060",
    )
    virus1_dose_gc: str | None = Field(
        default=None,
        title="Virus1 Dose (GC)",
        validation_alias="1987965412659076",
    )
    virus1_ap_mm: str | None = Field(
        default=None,
        title="Virus1 AP (mm)",
        validation_alias="7676949326417796",
    )
    virus1_ml_mm: str | None = Field(
        default=None,
        title="Virus1 ML (mm)",
        validation_alias="2047449792204676",
    )
    virus1_dv_mm: str | None = Field(
        default=None,
        title="Virus1 DV (mm)",
        validation_alias="6551049419575172",
    )
    virus1_dv_b_mm: str | None = Field(
        default=None,
        title="VIrus1 DV-b (mm)",
        validation_alias="1293960661127044",
    )
    virus1_stereotaxic_volume_injected_nl: str | None = Field(
        default=None,
        title="Virus1 Stereotaxic Volume Injected (nL)",
        validation_alias="2747643882065796",
    )
    virus2_injection_date: str | None = Field(
        default=None,
        title="Virus2 Injection Date",
        validation_alias="5797560288497540",
    )
    virus2_age_of_injection: str | None = Field(
        default=None,
        title="Virus2 Age of Injection",
        validation_alias="4108576491523972",
    )
    virus2_injection_type: str | None = Field(
        default=None,
        title="Virus2 Injection Type",
        validation_alias="3070266537103236",
    )
    virus2: str | None = Field(
        default=None, title="Virus2", validation_alias="3276091070304132"
    )
    virus2_ai_p_num: str | None = Field(
        default=None, title="Virus2 AiP#", validation_alias="3973741844664196"
    )
    virus2_id: str | None = Field(
        default=None, title="Virus2 ID", validation_alias="7779690697674628"
    )
    virus2_stock_titer_gc_ml: str | None = Field(
        default=None,
        title="Virus2 Stock Titer (GC/mL)",
        validation_alias="2150191163461508",
    )
    virus2_working_titer_gc_ml: str | None = Field(
        default=None,
        title="Virus2 Working Titer (GC/mL",
        validation_alias="822428977893252",
    )
    virus2_dose_gc: str | None = Field(
        default=None,
        title="Virus2 Dose (GC)",
        validation_alias="6653790790832004",
    )
    virus2_effective_titer_gc_ml: str | None = Field(
        default=None,
        title="Virus2 Effective Titer (GC/mL)",
        validation_alias="5011696052555652",
    )
    virus2_ap_mm: str | None = Field(
        default=None,
        title="Virus2 AP (mm)",
        validation_alias="2213733209165700",
    )
    virus2_ml_mm: str | None = Field(
        default=None,
        title="Virus2 ML (mm)",
        validation_alias="6717332836536196",
    )
    virus2_dv_mm: str | None = Field(
        default=None,
        title="Virus2 DV (mm)",
        validation_alias="4465533022850948",
    )
    virus2_dv_b_mm: str | None = Field(
        default=None,
        title="Virus2 DV-b (mm)",
        validation_alias="3545760474812292",
    )
    virus2_stereotaxic_volume_injected_nl: str | None = Field(
        default=None,
        title="Virus2 Stereotaxic Volume Injected (nL)",
        validation_alias="4239765226344324",
    )
    virus3_injection_date: str | None = Field(
        default=None,
        title="Virus3 Injection Date",
        validation_alias="4999443695751044",
    )
    virus3_age_of_injection: str | None = Field(
        default=None,
        title="Virus3 Age of Injection",
        validation_alias="8612176118894468",
    )
    virus3_injection_type: str | None = Field(
        default=None,
        title="Virus3 Injection Type",
        validation_alias="780508909752196",
    )
    virus3: str | None = Field(
        default=None, title="Virus3", validation_alias="4784000552882052"
    )
    virus3_ai_p_num: str | None = Field(
        default=None, title="Virus3 AiP#", validation_alias="1904875626860420"
    )
    virus3_id: str | None = Field(
        default=None, title="Virus3 ID", validation_alias="8688102315872132"
    )
    virus3_stock_titer_gc_ml: str | None = Field(
        default=None,
        title="Virus3 Stock Titer (GC/mL)",
        validation_alias="2532200739196804",
    )
    virus3_dose_gc: str | None = Field(
        default=None,
        title="Virus3 Dose (GC)",
        validation_alias="7035800366567300",
    )
    virus3_effective_titer_gc_ml: str | None = Field(
        default=None,
        title="Virus3 Effective Titer (GC/mL)",
        validation_alias="508096425185156",
    )
    virus3_ap_mm: str | None = Field(
        default=None,
        title="Virus3 AP (mm)",
        validation_alias="4361788087816068",
    )
    virus3_ml_mm: str | None = Field(
        default=None,
        title="Virus3 ML (mm)",
        validation_alias="8865387715186564",
    )
    virus3_dv_mm: str | None = Field(
        default=None,
        title="Virus3 DV (mm)",
        validation_alias="280400925511556",
    )
    virus3_dv_b_mm: str | None = Field(
        default=None,
        title="Virus3 DV-b (mm)",
        validation_alias="495844068380548",
    )
    virus3_stereotaxic_volume_injected_nl: str | None = Field(
        default=None,
        title="Virus3 Stereotaxic Volume Injected (nL)",
        validation_alias="7251243509436292",
    )
    virus4_injection_date: str | None = Field(
        default=None,
        title="Virus4 Injection Date",
        validation_alias="5914718843916164",
    )
    virus4_age_of_injection: str | None = Field(
        default=None,
        title="Virus4 Age of Injection",
        validation_alias="1411119216545668",
    )
    virus4_injection_type: str | None = Field(
        default=None,
        title="Virus4 Injection Type",
        validation_alias="7040618750758788",
    )
    virus4: str | None = Field(
        default=None, title="Virus4", validation_alias="2537019123388292"
    )
    virus4_id: str | None = Field(
        default=None, title="Virus4 ID", validation_alias="4788818937073540"
    )
    virus4_stock_titer_gc_ml: str | None = Field(
        default=None,
        title="Virus4 Stock Titer (GC/mL)",
        validation_alias="7497768258195332",
    )
    virus4_dose_gc: str | None = Field(
        default=None,
        title="Virus4 Dose (GC)",
        validation_alias="1868268723982212",
    )
    virus4_effective_titer_gc_ml: str | None = Field(
        default=None,
        title="Virus4 Effective Titer (GC/mL)",
        validation_alias="6371868351352708",
    )
    virus4_ap_mm: str | None = Field(
        default=None,
        title="Virus4 AP (mm)",
        validation_alias="4120068537667460",
    )
    virus4_ml_mm: str | None = Field(
        default=None,
        title="Virus4 ML (mm)",
        validation_alias="8623668165037956",
    )
    virus4_dv_mm: str | None = Field(
        default=None,
        title="Virus4 DV (mm)",
        validation_alias="460893840428932",
    )
    virus4_dv_b_mm: str | None = Field(
        default=None,
        title="Virus4 DV-b (mm)",
        validation_alias="4964493467799428",
    )
    stereotaxic_volume_injected_nl: str | None = Field(
        default=None,
        title="Stereotaxic Volume Injected (nL)",
        validation_alias="2712693654114180",
    )
    heparin_dose_u: str | None = Field(
        default=None,
        title="Heparin Dose (U)",
        validation_alias="5295955619303300",
    )
    perfused: str | None = Field(
        default=None, title="Perfused", validation_alias="1495493210230660"
    )
    perfusion_type: str | None = Field(
        default=None,
        title="Perfusion Type",
        validation_alias="3768626641325956",
    )
    perfusion_date: str | None = Field(
        default=None,
        title="Perfusion Date",
        validation_alias="4661977691410308",
    )
    age_of_perfusion: str | None = Field(
        default=None,
        title="Age of Perfusion",
        validation_alias="2410177877725060",
    )
    las_injection_notes: str | None = Field(
        default=None,
        title="LAS Injection Notes",
        validation_alias="8743364853714820",
    )
    las_perfusion_dissection_notes: str | None = Field(
        default=None,
        title="LAS Perfusion/Dissection Notes",
        validation_alias="6913777505095556",
    )
    gross_anatomy_notes_pre_processing: str | None = Field(
        default=None,
        title="Gross Anatomy Notes (Pre-Processing)",
        validation_alias="1284277970882436",
    )
    other_notes: str | None = Field(
        default=None, title="Other Notes", validation_alias="5787877598252932"
    )
    other_notes2: str | None = Field(
        default=None, title="Other Notes2", validation_alias="191596992876420"
    )
    neuro_glancer_link: str | None = Field(
        default=None,
        title="NeuroGlancer Link",
        validation_alias="3924157929574276",
    )
    good_labeling_sparsity: str | None = Field(
        default=None,
        title="Good Labeling Sparsity",
        validation_alias="743271656886148",
    )
    target_area_of_interest: str | None = Field(
        default=None,
        title="Target Area of Interest",
        validation_alias="8101845666140036",
    )
    investigator: str | None = Field(
        default=None, title="Investigator", validation_alias="3536077784567684"
    )
    project_code: str | None = Field(
        default=None, title="Project Code", validation_alias="412349291515780"
    )
    project_name: str | None = Field(
        default=None, title="Project Name", validation_alias="4915948918886276"
    )
    death_health_issues: str | None = Field(
        default=None,
        title="Death/Health Issues",
        validation_alias="5999092837601156",
    )


class SampleTracking(BaseModel):
    """Sample Tracking Sheet Information."""

    model_config = ConfigDict(coerce_numbers_to_str=True)
    external_sample: str | None = Field(
        default=None,
        title="External Sample",
        validation_alias="2118380215553924",
    )
    screening_status: str | None = Field(
        default=None,
        title="Screening status",
        validation_alias="3700590659276676",
    )
    status: str | None = Field(
        default=None, title="Status", validation_alias="1212189360738180"
    )
    sample: str | None = Field(
        default=None, title="Sample", validation_alias="7747879749767044"
    )
    genotype: str | None = Field(
        default=None, title="Genotype", validation_alias="4370180029239172"
    )
    processing_lead: str | None = Field(
        default=None,
        title="Processing Lead",
        validation_alias="6841688894951300",
    )
    project: str | None = Field(
        default=None, title="Project", validation_alias="8391723336814468"
    )
    project_description: str | None = Field(
        default=None,
        title="Project description",
        validation_alias="4726059059941252",
    )
    project_name: str | None = Field(
        default=None, title="Project name", validation_alias="1788928007556996"
    )
    label: str | None = Field(
        default=None, title="Label", validation_alias="8873779656609668"
    )
    age_of_injection: str | None = Field(
        default=None,
        title="Age of Injection",
        validation_alias="77686634401668",
    )
    virus_dose: str | None = Field(
        default=None, title="Virus Dose", validation_alias="1324377418190724"
    )
    dcm_delipidation_start: str | None = Field(
        default=None,
        title="DCM Delipidation Start",
        validation_alias="2329486448086916",
    )
    dcm_delipidation_end: str | None = Field(
        default=None,
        title="DCM Delipidation End",
        validation_alias="6833086075457412",
    )
    sbip_delipidation_start: str | None = Field(
        default=None,
        title="SBiP Delipidation Start",
        validation_alias="1203586541244292",
    )
    sbip_delipidation_end: str | None = Field(
        default=None,
        title="SBiP Delipidation End",
        validation_alias="5707186168614788",
    )
    immuno_primary_ab_start_date: str | None = Field(
        default=None,
        title="Immuno: Primary Ab Start Date",
        validation_alias="1581397634404228",
    )
    immuno_primary_antibody1: str | None = Field(
        default=None,
        title="Immuno: Primary Antibody1",
        validation_alias="3455386354929540",
    )
    mass_of_primary_antibody1_used_per_brain_ug: str | None = Field(
        default=None,
        title="Mass of Primary Antibody1 used per Brain (ug)",
        validation_alias="8828048989179780",
    )
    primary_antibody1_catalog_num: str | None = Field(
        default=None,
        title="Primary Antibody1 Catalog #",
        validation_alias="8164547174027140",
    )
    primary_antibody1_lot_num: str | None = Field(
        default=None,
        title="Primary Antibody1 Lot #",
        validation_alias="4058955958407044",
    )
    immuno_primary_antibody2: str | None = Field(
        default=None,
        title="Immuno: Primary Antibody2",
        validation_alias="4619349745684356",
    )
    mass_of_primary_antibody2_used_per_brain_ug: str | None = Field(
        default=None,
        title="Mass of Primary Antibody2 used per Brain (ug)",
        validation_alias="2367549931999108",
    )
    primary_antibody2_catalog_num: str | None = Field(
        default=None,
        title="Primary Antibody2 Catalog #",
        validation_alias="6871149559369604",
    )
    primary_antibody2_lot_num: str | None = Field(
        default=None,
        title="Primary Antibody2 Lot #",
        validation_alias="1241650025156484",
    )
    immuno_primary_antibody3: str | None = Field(
        default=None,
        title="Immuno: Primary Antibody3",
        validation_alias="5745249652526980",
    )
    mass_of_primary_antibody3_used_per_brain_ug: str | None = Field(
        default=None,
        title="Mass of Primary Antibody3 used per Brain (ug)",
        validation_alias="3493449838841732",
    )
    primary_antibody3_catalog_num: str | None = Field(
        default=None,
        title="Primary Antibody3 Catalog #",
        validation_alias="7997049466212228",
    )
    primary_antibody3_lot_num: str | None = Field(
        default=None,
        title="Primary Antibody3 Lot #",
        validation_alias="678700071735172",
    )
    primary_antibody_rrid: str | None = Field(
        default=None,
        title="Primary Antibody RRID",
        validation_alias="2585472132927364",
    )
    immuno_secondary_ab_start_date: str | None = Field(
        default=None,
        title="Immuno: Secondary Ab Start Date",
        validation_alias="6084997261774724",
    )
    immuno_secondary_antibody1: str | None = Field(
        default=None,
        title="Immuno: Secondary Antibody1",
        validation_alias="7958985982300036",
    )
    mass_of_secondary_antibody1_used_per_brain_ug: str | None = Field(
        default=None,
        title="Mass of Secondary Antibody1 used per Brain (ug)",
        validation_alias="8331167712366468",
    )
    secondary_antibody1_catalog_num: str | None = Field(
        default=None,
        title="Secondary Antibody1 Catalog #",
        validation_alias="3933310985129860",
    )
    secondary_antibody1_lot_num: str | None = Field(
        default=None,
        title="Secondary Antibody1 Lot #",
        validation_alias="8562555585777540",
    )
    immuno_secondary_antibody2: str | None = Field(
        default=None,
        title="Immuno: Secondary Antibody2",
        validation_alias="7619773901787012",
    )
    mass_of_secondary_antibody2_used_per_brain_ug: str | None = Field(
        default=None,
        title="Mass of Secondary Antibody2 used per Brain (ug)",
        validation_alias="2671906346979204",
    )
    secondary_antibody2_catalog_num: str | None = Field(
        default=None,
        title="Secondary Antibody2 Catalog #",
        validation_alias="4923706160664452",
    )
    secondary_antibody2_lot_num: str | None = Field(
        default=None,
        title="Secondary Antibody2 Lot #",
        validation_alias="420106533293956",
    )
    immuno_secondary_antibody3: str | None = Field(
        default=None,
        title="Immuno: Secondary Antibody3",
        validation_alias="1990274367573892",
    )
    mass_of_secondary_antibody3_used_per_brain_ug: str | None = Field(
        default=None,
        title="Mass of Secondary Antibody3 used per Brain (ug)",
        validation_alias="6049606067507076",
    )
    secondary_antibody3_catalog_num: str | None = Field(
        default=None,
        title="Secondary Antibody3 Catalog #",
        validation_alias="1546006440136580",
    )
    secondary_antibody3_lot_num: str | None = Field(
        default=None,
        title="Secondary Antibody3 Lot #",
        validation_alias="7175505974349700",
    )
    secondary_antibody_rrid: str | None = Field(
        default=None,
        title="Secondary Antibody RRID",
        validation_alias="7089071760297860",
    )
    fluorophore1: str | None = Field(
        default=None, title="Fluorophore1", validation_alias="7608858729992068"
    )
    fluorophore2: str | None = Field(
        default=None, title="Fluorophore2", validation_alias="4242074181259140"
    )
    fluorophore3: str | None = Field(
        default=None, title="Fluorophore3", validation_alias="6493873994944388"
    )
    fluorophore_t: str | None = Field(
        default=None, title="FluorophoreT", validation_alias="6497713993502596"
    )
    gelation_mbs_start: str | None = Field(
        default=None,
        title="Gelation: MBS Start",
        validation_alias="640636587822980",
    )
    gelation_mbs_end: str | None = Field(
        default=None,
        title="Gelation: MBS End",
        validation_alias="5144236215193476",
    )
    gelation_ac_x_start: str | None = Field(
        default=None,
        title="Gelation: AcX Start",
        validation_alias="2892436401508228",
    )
    gelation_ac_x_end: str | None = Field(
        default=None,
        title="Gelation: AcX End",
        validation_alias="7396036028878724",
    )
    gelation_pbs_wash_start: str | None = Field(
        default=None,
        title="Gelation: PBS Wash Start",
        validation_alias="1766536494665604",
    )
    gelation_pbs_wash_end: str | None = Field(
        default=None,
        title="Gelation: PBS Wash End",
        validation_alias="6270136122036100",
    )
    gelation_stock_xva_044_equilibration_start: str | None = Field(
        default=None,
        title="Gelation: Stock X + VA-044 Equilibration  Start",
        validation_alias="4018336308350852",
    )
    gelation_stock_xva_044_equilibration_end: str | None = Field(
        default=None,
        title="Gelation: Stock X + VA-044 Equilibration End",
        validation_alias="8521935935721348",
    )
    gelation_prok_rt_start: str | None = Field(
        default=None,
        title="Gelation +  ProK RT Start",
        validation_alias="359161611112324",
    )
    gelation_prok_rt_end: str | None = Field(
        default=None,
        title="Gelation +  ProK RT End",
        validation_alias="4862761238482820",
    )
    duration_days: str | None = Field(
        default=None,
        title="Duration (days)",
        validation_alias="2610961424797572",
    )
    gelation_add_l_prok_37c_start: str | None = Field(
        default=None,
        title="Gelation + Add'l ProK 37C Start",
        validation_alias="7114561052168068",
    )
    gelation_add_l_prok_37c_end: str | None = Field(
        default=None,
        title="Gelation + Add'l ProK 37C End",
        validation_alias="1485061517954948",
    )
    duration_days_gelation_add_l_prok_37c: str | None = Field(
        default=None,
        title="Duration (days) Gelation + Add'l ProK 37C",
        validation_alias="5988661145325444",
    )
    pbs_wash_start: str | None = Field(
        default=None,
        title="PBS Wash Start",
        validation_alias="3736861331640196",
    )
    pbs_wash_end: str | None = Field(
        default=None, title="PBS Wash End", validation_alias="8240460959010692"
    )
    date_of_storage_in_pbs_az_0_05_4c: str | None = Field(
        default=None,
        title="Date of Storage in PBS Az 0.05% @4C",
        validation_alias="922111564533636",
    )
    notes: str | None = Field(
        default=None, title="Notes", validation_alias="5425711191904132"
    )
    notes_ii: str | None = Field(
        default=None, title="Notes II", validation_alias="3173911378218884"
    )
    notes_iii: str | None = Field(
        default=None, title="Notes III", validation_alias="7677511005589380"
    )


class ImagingQueue(BaseModel):
    """Imaging Queue Sheet Information."""

    model_config = ConfigDict(coerce_numbers_to_str=True)
    count: str | None = Field(
        default=None, title="Count", validation_alias="7390464688738180"
    )
    sample: str | None = Field(
        default=None, title="Sample", validation_alias="8172469210795908"
    )
    one_x_imaging_date: str | None = Field(
        default=None,
        title="1X Imaging Date",
        validation_alias="7751950453215108",
    )
    imaging_start_date: str | None = Field(
        default=None,
        title="Imaging Start Date",
        validation_alias="5987409380462468",
    )
    imaging_start_time: str | None = Field(
        default=None,
        title="Imaging Start Time",
        validation_alias="7358218151169924",
    )
    drop_off_date: str | None = Field(
        default=None,
        title="Drop-off Date",
        validation_alias="3668869583425412",
    )
    imaging_end_date: str | None = Field(
        default=None,
        title="Imaging End Date",
        validation_alias="7010871500033924",
    )
    imaging_end_time: str | None = Field(
        default=None,
        title="Imaging End Time",
        validation_alias="8933908273205124",
    )
    imaging_buffer: str | None = Field(
        default=None,
        title="Imaging Buffer",
        validation_alias="854119816318852",
    )
    microscope: str | None = Field(
        default=None, title="Microscope", validation_alias="5357719443689348"
    )
    status: str | None = Field(
        default=None, title="Status", validation_alias="3105919630004100"
    )
    genotype: str | None = Field(
        default=None, title="Genotype", validation_alias="6451094460780420"
    )
    label: str | None = Field(
        default=None, title="Label", validation_alias="4199294647095172"
    )
    fluorophore: str | None = Field(
        default=None, title="Fluorophore", validation_alias="8702894274465668"
    )
    signal_channel_s: str | None = Field(
        default=None,
        title="Signal channel(s)",
        validation_alias="7125805770428292",
    )
    auto_fluorescence_channel_s: str | None = Field(
        default=None,
        title="Auto-fluorescence channel(s)",
        validation_alias="3295611976634244",
    )
    focus_n_mm: str | None = Field(
        default=None, title="Focus (N mm)", validation_alias="5958720178573188"
    )
    etl_offset: str | None = Field(
        default=None, title="ETL Offset", validation_alias="3706920364887940"
    )
    notes: str | None = Field(
        default=None, title="Notes", validation_alias="7609519257374596"
    )
    notes_1: str | None = Field(
        default=None, title="Notes (1)", validation_alias="1980019723161476"
    )
    verified_mouse_tracker_for_metadata_intake: str | None = Field(
        default=None,
        title="Verified Mouse Tracker for Metadata Intake",
        validation_alias="6483619350531972",
    )
    notes_on_missing_metadata: str | None = Field(
        default=None,
        title="notes on missing metadata",
        validation_alias="4231819536846724",
    )


class QcSheet(BaseModel):
    """QC Sheet Information."""

    model_config = ConfigDict(coerce_numbers_to_str=True)
    sample: str | None = Field(
        default=None, title="Sample", validation_alias="5706446774423428"
    )
    imaging_priority: str | None = Field(
        default=None,
        title="Imaging priority",
        validation_alias="1303602456203140",
    )
    date_sent_for_1x_imaging: str | None = Field(
        default=None,
        title="Date Sent for 1X Imaging",
        validation_alias="1724279648112516",
    )
    date_of_tissue_processing_completion: str | None = Field(
        default=None,
        title="Date of Tissue Processing Completion",
        validation_alias="6470842761645956",
    )
    status: str | None = Field(
        default=None, title="Status", validation_alias="4750198374174596"
    )
    genotype: str | None = Field(
        default=None, title="Genotype", validation_alias="3454646960738180"
    )
    label: str | None = Field(
        default=None, title="Label", validation_alias="5890473712717700"
    )
    project_description: str | None = Field(
        default=None,
        title="Project Description",
        validation_alias="7958246588108676",
    )
    perfusion_date: str | None = Field(
        default=None,
        title="Perfusion Date",
        validation_alias="639897193631620",
    )
    las_injection_notes: str | None = Field(
        default=None,
        title="LAS Injection Notes",
        validation_alias="6038744703127428",
    )
    las_perfusion_dissection_notes: str | None = Field(
        default=None,
        title="LAS Perfusion/Dissection Notes",
        validation_alias="5143496821002116",
    )
    perfusion_dissection_quality_notes: str | None = Field(
        default=None,
        title="Perfusion / Dissection Quality Notes",
        validation_alias="2891697007316868",
    )
    perfusion_pass_fail: str | None = Field(
        default=None,
        title="Perfusion Pass/Fail",
        validation_alias="972195122335620",
    )
    labeling_density_notes_olympus_mxv10: str | None = Field(
        default=None,
        title="Labeling Density Notes (Olympus MXV10)",
        validation_alias="3786944889442180",
    )
    durotomy_tissue_damage_notes: str | None = Field(
        default=None,
        title="Durotomy: Tissue Damage Notes",
        validation_alias="5475794749706116",
    )
    immuno_gross_anatomy_notes: str | None = Field(
        default=None,
        title="Immuno Gross Anatomy Notes",
        validation_alias="3223994936020868",
    )
    immuno_pass_fail: str | None = Field(
        default=None,
        title="Immuno Pass/Fail",
        validation_alias="6262033424355204",
    )
    digestion_notes: str | None = Field(
        default=None,
        title="Digestion Notes",
        validation_alias="2146233072963460",
    )
    digestion_pass_fail: str | None = Field(
        default=None,
        title="Digestion Pass/Fail",
        validation_alias="6649832700333956",
    )
    special_notes: str | None = Field(
        default=None,
        title="Special Notes",
        validation_alias="4637260017602436",
    )
    brain_size_at_1x_imaging: str | None = Field(
        default=None,
        title="Brain Size at 1X Imaging",
        validation_alias="6227879275483012",
    )
    one_x_screening_link: str | None = Field(
        default=None,
        title="1X Screening Link",
        validation_alias="3976079461797764",
    )
    investigator: str | None = Field(
        default=None, title="Investigator", validation_alias="3975198807461764"
    )
    project_name: str | None = Field(
        default=None, title="Project Name", validation_alias="4670982861393796"
    )
    surface_labeling: str | None = Field(
        default=None,
        title="Surface labeling",
        validation_alias="455954645946244",
    )
    vascular_labeling: str | None = Field(
        default=None,
        title="Vascular labeling",
        validation_alias="4959554273316740",
    )
    no_artifacts: str | None = Field(
        default=None,
        title="No Artifacts?",
        validation_alias="4820504391929732",
    )
    targeted_sparsity: str | None = Field(
        default=None,
        title="Targeted Sparsity",
        validation_alias="2707754459631492",
    )
    no_surface_labeling: str | None = Field(
        default=None,
        title="No Surface Labeling?",
        validation_alias="8479679089168260",
    )
    no_vascular_labeling: str | None = Field(
        default=None,
        title="No Vascular Labeling?",
        validation_alias="316904764559236",
    )
    targeted_sparsity_q: str | None = Field(
        default=None,
        title="Targeted Sparsity?",
        validation_alias="2568704578244484",
    )
    one_x_review_pass_fail: str | None = Field(
        default=None,
        title="1X Review Pass/Fail",
        validation_alias="7072304205614980",
    )
    one_x_screening_notes_platform_lead: str | None = Field(
        default=None,
        title="1x screening notes - Platform lead",
        validation_alias="6546073897439108",
    )
    one_x_screening_notes_sample_processing_r_a: str | None = Field(
        default=None,
        title="1x screening notes - Sample processing RA",
        validation_alias="4294274083753860",
    )
    one_x_screening_notes_investigator: str | None = Field(
        default=None,
        title="1x screening notes - Investigator",
        validation_alias="8797873711124356",
    )
    five_x_imaging_date: str | None = Field(
        default=None,
        title="5x Imaging Date",
        validation_alias="361522735124356",
    )


class ExaSPIMInfo(BaseModel):
    """All exaSPIM Information for Specimen ID"""

    mouse_tracker_info: List[MouseTracker] = Field(default_factory=list)
    sample_tracking_info: List[SampleTracking] = Field(default_factory=list)
    imaging_queue_info: List[ImagingQueue] = Field(default_factory=list)
    qc_sheet_info: List[QcSheet] = Field(default_factory=list)
