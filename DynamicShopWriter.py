import csv
import os

# Below is the data set up in nested categories.The top level determines the DEF type to be output into the CSV file on creation.The next level down# Values below in the pair ie[1, 1] = [Quantity, Frequency] Frequency 1 - 10 with 10 being always
#This script is designed for the user to update / create CSV files from a singular location.
categories = {
    #DEF-Type# = "ComponentType": "" from JSON File
    "HeatSink": {
        #Category#
        "Engines": {
            "emod_engineslots_tunedlight": [1, 1],
            "emod_engineslots_xl_periphery": [1, 1],
            "emod_engineslots_light": [1, 1],
            "emod_engineslots_std": [1, 1],
            "emod_engineslots_xl_center": [1, 1]
        },
        "HeatSinks": {
            "Gear_HeatSink_Generic_Double": [1, 1],
            "Gear_HeatSink_Generic_Standard": [1, 1]
        },
        "EngineCore": {
            "emod_engine_010": [1, 1],
            "emod_engine_015": [1, 1],
            "emod_engine_020": [1, 1],
            "emod_engine_025": [1, 1],
            "emod_engine_030": [1, 1],
            "emod_engine_035": [1, 1],
            "emod_engine_040": [1, 1],
            "emod_engine_045": [1, 1],
            "emod_engine_050": [1, 1],
            "emod_engine_055": [1, 1],
            "emod_engine_060": [1, 1],
            "emod_engine_065": [1, 1],
            "emod_engine_070": [1, 1],
            "emod_engine_075": [1, 1],
            "emod_engine_080": [1, 1],
            "emod_engine_085": [1, 1],
            "emod_engine_090": [1, 1],
            "emod_engine_095": [1, 1],
            "emod_engine_100": [1, 1],
            "emod_engine_105": [1, 1],
            "emod_engine_110": [1, 1],
            "emod_engine_115": [1, 1],
            "emod_engine_120": [1, 1],
            "emod_engine_125": [1, 1],
            "emod_engine_130": [1, 1],
            "emod_engine_135": [1, 1],
            "emod_engine_140": [1, 1],
            "emod_engine_145": [1, 1],
            "emod_engine_150": [1, 1],
            "emod_engine_155": [1, 1],
            "emod_engine_160": [1, 1],
            "emod_engine_165": [1, 1],
            "emod_engine_170": [1, 1],
            "emod_engine_175": [1, 1],
            "emod_engine_180": [1, 1],
            "emod_engine_185": [1, 1],
            "emod_engine_190": [1, 1],
            "emod_engine_195": [1, 1],
            "emod_engine_200": [1, 1],
            "emod_engine_205": [1, 1],
            "emod_engine_210": [1, 1],
            "emod_engine_215": [1, 1],
            "emod_engine_220": [1, 1],
            "emod_engine_225": [1, 1],
            "emod_engine_230": [1, 1],
            "emod_engine_235": [1, 1],
            "emod_engine_240": [1, 1],
            "emod_engine_245": [1, 1],
            "emod_engine_250": [1, 1],
            "emod_engine_255": [1, 1],
            "emod_engine_260": [1, 1],
            "emod_engine_265": [1, 1],
            "emod_engine_270": [1, 1],
            "emod_engine_275": [1, 1],
            "emod_engine_280": [1, 1],
            "emod_engine_285": [1, 1],
            "emod_engine_290": [1, 1],
            "emod_engine_295": [1, 1],
            "emod_engine_300": [1, 1],
            "emod_engine_305": [1, 1],
            "emod_engine_310": [1, 1],
            "emod_engine_315": [1, 1],
            "emod_engine_320": [1, 1],
            "emod_engine_325": [1, 1],
            "emod_engine_330": [1, 1],
            "emod_engine_335": [1, 1],
            "emod_engine_340": [1, 1],
            "emod_engine_345": [1, 1],
            "emod_engine_350": [1, 1],
            "emod_engine_355": [1, 1],
            "emod_engine_360": [1, 1],
            "emod_engine_365": [1, 1],
            "emod_engine_370": [1, 1],
            "emod_engine_375": [1, 1],
            "emod_engine_380": [1, 1],
            "emod_engine_385": [1, 1],
            "emod_engine_390": [1, 1],
            "emod_engine_395": [1, 1],
            "emod_engine_400": [1, 1],
        },
        "HSKits": {
            "emod_kit_dhs": [1, 1],
            "emod_kit_shs": [1, 1]
        },
    },
    "Weapon": {
        "Lasers": {
            "Weapon_Laser_LargeLaser_2-Intek": [1, 1],
            "Weapon_Laser_LargeLaser_2-Magna": [1, 1],
            "Weapon_Laser_MediumLaser_0-STOCK": [1, 1],
            "Weapon_Laser_MediumLaser_1-ExoStar": [1, 1],
            "Weapon_Laser_MediumLaser_1-Intek": [1, 1],
            "Weapon_Laser_MediumLaser_1-Magna": [1, 1],
            "Weapon_Laser_MediumLaser_2-Diverse_Optics": [1, 1],
            "Weapon_Laser_MediumLaser_2-ExoStar": [1, 1],
            "Weapon_Laser_MediumLaser_2-Intek": [1, 1],
            "Weapon_Laser_MediumLaser_2-Magna": [1, 1],
            "Weapon_Laser_MediumLaser_3-Diverse_Optics": [1, 1],
            "Weapon_Laser_SmallLaser_0-STOCK": [1, 1],
            "Weapon_Laser_SmallLaser_1-Diverse_Optics": [1, 1],
            "Weapon_Laser_SmallLaser_1-ExoStar": [1, 1],
            "Weapon_Laser_SmallLaser_1-Magna": [1, 1],
            "Weapon_Laser_SmallLaser_2-Diverse_Optics": [1, 1],
            "Weapon_Laser_SmallLaser_2-ExoStar": [1, 1],
            "Weapon_Laser_SmallLaser_2-Intek": [1, 1],
            "Weapon_Laser_SmallLaser_2-Magna": [1, 1],
            "Weapon_Laser_SmallLaser_3-Intek": [1, 1],
        },
        "ERLasers": {
            "Weapon_Laser_SmallLaserER_0-STOCK": [1, 1],
            "Weapon_Laser_SmallLaserER_1-Diverse_Optics": [1, 1],
            "Weapon_Laser_SmallLaserER_2-BlazeFire": [1, 1],
            "Weapon_Laser_MediumLaserER_0-STOCK": [1, 1],
            "Weapon_Laser_MediumLaserER_1-MagnaVI": [1, 1],
            "Weapon_Laser_MediumLaserER_2-BrightBloom": [1, 1],
            "Weapon_Laser_LargeLaserER_0-STOCK": [1, 1],
            "Weapon_Laser_LargeLaserER_1-Blankenburg25": [1, 1],
            "Weapon_Laser_LargeLaserER_2-BlazeFire": [1, 1],
        },
        "PulseLasers": {
            "Weapon_Laser_LargeLaserPulse_0-STOCK": [1, 1],
            "Weapon_Laser_LargeLaserPulse_1-Thunderbolt12": [1, 1],
            "Weapon_Laser_LargeLaserPulse_2-Exostar": [1, 1],
            "Weapon_Laser_MediumLaserPulse_0-STOCK": [1, 1],
            "Weapon_Laser_MediumLaserPulse_1-RakerIV": [1, 1],
            "Weapon_Laser_MediumLaserPulse_2-Magna400P": [1, 1],
            "Weapon_Laser_SmallLaserPulse_0-STOCK": [1, 1],
            "Weapon_Laser_SmallLaserPulse_1-Maxell": [1, 1],
            "Weapon_Laser_SmallLaserPulse_2-Magna200P": [1, 1],
        },
        "PPC": {
            "Weapon_PPC_PPC_0-STOCK": [1, 1],
            "Weapon_PPC_PPC_1-Ceres_Arms": [1, 1],
            "Weapon_PPC_PPC_1-Donal": [1, 1],
            "Weapon_PPC_PPC_1-Tiegart": [1, 1],
            "Weapon_PPC_PPC_2-Ceres_Arms": [1, 1],
            "Weapon_PPC_PPC_2-Donal": [1, 1],
            "Weapon_PPC_PPC_2-Tiegart": [1, 1],
            "Weapon_PPC_PPCER_0-STOCK": [1, 1],
            "Weapon_PPC_PPCER_1-MagnaFirestar": [1, 1],
            "Weapon_PPC_PPCER_2-TiegartMagnum": [1, 1],
            "Weapon_PPC_PPCSnub_0-STOCK": [1, 1],
            "Weapon_PPC_PPCSnub_1-Ceres_Arms": [1, 1],
            "Weapon_PPC_PPCSnub_1-Donal": [1, 1],
            "Weapon_PPC_PPCSnub_1-Magna": [1, 1],
            "Weapon_PPC_PPCSnub_2-Ceres_Arms": [1, 1],
            "Weapon_PPC_PPCSnub_2-Donal": [1, 1],
            "Weapon_PPC_PPCSnub_2-Magna": [1, 1],
        },
        "Autocannon": {
            "Weapon_Autocannon_AC2_0-STOCK": [1, 1],
            "Weapon_Autocannon_AC2_1-Defiance": [1, 1],
            "Weapon_Autocannon_AC2_1-Federated": [1, 1],
            "Weapon_Autocannon_AC2_1-Kali_Yama": [1, 1],
            "Weapon_Autocannon_AC2_1-Mydron": [1, 1],
            "Weapon_Autocannon_AC2_2-Defiance": [1, 1],
            "Weapon_Autocannon_AC2_2-Federated": [1, 1],
            "Weapon_Autocannon_AC2_2-Imperator": [1, 1],
            "Weapon_Autocannon_AC2_2-Kali_Yama": [1, 1],
            "Weapon_Autocannon_AC2_2-Mydron": [1, 1],
            "Weapon_Autocannon_AC2_3-Imperator": [1, 1],
            "Weapon_Autocannon_AC5_0-STOCK": [1, 1],
            "Weapon_Autocannon_AC5_1-Defiance": [1, 1],
            "Weapon_Autocannon_AC5_1-Federated": [1, 1],
            "Weapon_Autocannon_AC5_1-Imperator": [1, 1],
            "Weapon_Autocannon_AC5_1-Kali_Yama": [1, 1],
            "Weapon_Autocannon_AC5_2-Defiance": [1, 1],
            "Weapon_Autocannon_AC5_2-Federated": [1, 1],
            "Weapon_Autocannon_AC5_2-Imperator": [1, 1],
            "Weapon_Autocannon_AC5_2-Kali_Yama": [1, 1],
            "Weapon_Autocannon_AC5_2-Mydron": [1, 1],
            "Weapon_Autocannon_AC5_3-Mydron": [1, 1],
        },
        "Autocannon_Large": {
            "Weapon_Autocannon_AC10_0-STOCK": [1, 1],
            "Weapon_Autocannon_AC10_1-Defiance": [1, 1],
            "Weapon_Autocannon_AC10_1-Imperator": [1, 1],
            "Weapon_Autocannon_AC10_1-Kali_Yama": [1, 1],
            "Weapon_Autocannon_AC10_1-Mydron": [1, 1],
            "Weapon_Autocannon_AC10_2-Defiance": [1, 1],
            "Weapon_Autocannon_AC10_2-Federated": [1, 1],
            "Weapon_Autocannon_AC10_2-Imperator": [1, 1],
            "Weapon_Autocannon_AC10_2-Kali_Yama": [1, 1],
            "Weapon_Autocannon_AC10_2-Mydron": [1, 1],
            "Weapon_Autocannon_AC10_3-Federated": [1, 1],
            "Weapon_Autocannon_AC20_0-STOCK": [1, 1],
            "Weapon_Autocannon_AC20_1-Defiance": [1, 1],
            "Weapon_Autocannon_AC20_1-Federated": [1, 1],
            "Weapon_Autocannon_AC20_1-Imperator": [1, 1],
            "Weapon_Autocannon_AC20_1-Mydron": [1, 1],
            "Weapon_Autocannon_AC20_2-Defiance": [1, 1],
            "Weapon_Autocannon_AC20_2-Federated": [1, 1],
            "Weapon_Autocannon_AC20_2-Imperator": [1, 1],
            "Weapon_Autocannon_AC20_2-Kali_Yama": [1, 1],
            "Weapon_Autocannon_AC20_2-Mydron": [1, 1],
            "Weapon_Autocannon_AC20_3-Kali_Yama": [1, 1],
            "Weapon_Autocannon_AC20_SPECIAL-Victoria": [1, 1],
        },
        "UAC": {
            "Weapon_Autocannon_UAC2_0-STOCK": [1, 1],
            "Weapon_Autocannon_UAC2_1-Imperator": [1, 1],
            "Weapon_Autocannon_UAC2_2-Imperator": [1, 1],
            "Weapon_Autocannon_UAC5_0-STOCK": [1, 1],
            "Weapon_Autocannon_UAC5_1-Mydron": [1, 1],
            "Weapon_Autocannon_UAC5_2-Mydron": [1, 1],
            "Weapon_Autocannon_UAC10_0-STOCK": [1, 1],
            "Weapon_Autocannon_UAC10_1-Federated": [1, 1],
            "Weapon_Autocannon_UAC10_2-Federated": [1, 1],
            "Weapon_Autocannon_UAC20_0-STOCK": [1, 1],
            "Weapon_Autocannon_UAC20_1-Kali_Yama": [1, 1],
            "Weapon_Autocannon_UAC20_2-Kali_Yama": [1, 1],
        },
        "LBX": {
            "Weapon_Autocannon_LB2X_0-STOCK": [1, 1],
            "Weapon_Autocannon_LB2X_1-Defiance": [1, 1],
            "Weapon_Autocannon_LB2X_2-Defiance": [1, 1],
            "Weapon_Autocannon_LB5X_0-STOCK": [1, 1],
            "Weapon_Autocannon_LB5X_1-GM": [1, 1],
            "Weapon_Autocannon_LB5X_2-GM": [1, 1],
            "Weapon_Autocannon_LB10X_0-STOCK": [1, 1],
            "Weapon_Autocannon_LB10X_1-Western": [1, 1],
            "Weapon_Autocannon_LB10X_2-Western": [1, 1],
            "Weapon_Autocannon_LB20X_0-STOCK": [1, 1],
            "Weapon_Autocannon_LB20X_1-Shengli_Arms": [1, 1],
            "Weapon_Autocannon_LB20X_2-Shengli_Arms": [1, 1],
        },
        "HVAC": {
            "Weapon_Autocannon_HVAC2_0-STOCK": [1, 1],
            "Weapon_Autocannon_HVAC5_0-STOCK": [1, 1],
            "Weapon_Autocannon_HVAC10_0-STOCK": [1, 1],
            "Weapon_Autocannon_HVAC20_0-STOCK": [1, 1],
        },
        "MachineGun": {
            "Weapon_MachineGun_MachineGun_0-STOCK": [1, 1],
            "Weapon_MachineGun_MachineGun_1-Brigadier": [1, 1],
            "Weapon_MachineGun_MachineGun_1-VMI": [1, 1],
            "Weapon_MachineGun_MachineGun_2-Brigadier": [1, 1],
            "Weapon_MachineGun_MachineGun_2-VMI": [1, 1],
        },
        "Gauss": {
            "Weapon_Gauss_Gauss_Silverbullet": [1, 1],
            "Weapon_Gauss_Heavy_0-STOCK": [1, 1],
            "Weapon_Gauss_ImprovedHeavy_0-STOCK": [1, 1],
            "Weapon_Gauss_Gauss_0-STOCK": [1, 1],
            "Weapon_Gauss_Gauss_1-M7": [1, 1],
            "Weapon_Gauss_Gauss_2-M9": [1, 1],
        },
        "Rifle": {
            "Weapon_Autocannon_HeavyRifle": [1, 1],
            "Weapon_Autocannon_MediumRifle": [1, 1],
            "Weapon_Autocannon_LightRifle": [1, 1]
        },
        "SRM": {
            "Weapon_SRM_SRM2_0-STOCK": [1, 1],
            "Weapon_SRM_SRM2_1-Holly": [1, 1],
            "Weapon_SRM_SRM2_1-Irian": [1, 1],
            "Weapon_SRM_SRM2_2-Holly": [1, 1],
            "Weapon_SRM_SRM2_2-Irian": [1, 1],
            "Weapon_SRM_SRM2_2-Valiant": [1, 1],
            "Weapon_SRM_SRM2_3-Valiant": [1, 1],
            "Weapon_SRM_SRM4_0-STOCK": [1, 1],
            "Weapon_SRM_SRM4_1-Holly"
            "Weapon_SRM_SRM4_1-Irian": [1, 1],
            "Weapon_SRM_SRM4_2-Holly": [1, 1],
            "Weapon_SRM_SRM4_2-Irian": [1, 1],
            "Weapon_SRM_SRM4_2-Valiant": [1, 1],
            "Weapon_SRM_SRM4_3-Valiant": [1, 1],
            "Weapon_SRM_SRM6_0-STOCK": [1, 1],
            "Weapon_SRM_SRM6_1-Holly": [1, 1],
            "Weapon_SRM_SRM6_1-Irian": [1, 1],
            "Weapon_SRM_SRM6_2-Holly": [1, 1],
            "Weapon_SRM_SRM6_2-Irian": [1, 1],
            "Weapon_SRM_SRM6_2-Valiant": [1, 1],
            "Weapon_SRM_SRM6_3-Valiant": [1, 1],
        },
        "StreakSRM": {
            "Weapon_SRM_SRM2_Streak": [1, 1],
            "Weapon_SRM_SRM6_Streak": [1, 1],
            "Weapon_SRM_SRM4_Streak": [1, 1],
        },
        "StreakLRM": {

        },
        "MRM": {
            "Weapon_MRM_MRM10": [1, 1],
            "Weapon_MRM_MRM20": [1, 1],
            "Weapon_MRM_MRM30": [1, 1],
            "Weapon_MRM_MRM40": [1, 1],
        },
        "LRM": {
            "Weapon_LRM_LRM5_0-STOCK": [1, 1],
            "Weapon_LRM_LRM5_1-Delta": [1, 1],
            "Weapon_LRM_LRM5_1-LongFire": [1, 1],
            "Weapon_LRM_LRM5_1-Telos": [1, 1],
            "Weapon_LRM_LRM5_2-Delta": [1, 1],
            "Weapon_LRM_LRM5_2-LongFire": [1, 1],
            "Weapon_LRM_LRM5_2-Telos": [1, 1],
            "Weapon_LRM_LRM5_2-Zeus": [1, 1],
            "Weapon_LRM_LRM5_3-Zeus": [1, 1],
            "Weapon_LRM_LRM10_0-STOCK": [1, 1],
            "Weapon_LRM_LRM10_1-Delta": [1, 1],
            "Weapon_LRM_LRM10_1-LongFire": [1, 1],
            "Weapon_LRM_LRM10_1-Telos": [1, 1],
            "Weapon_LRM_LRM10_2-Delta": [1, 1],
            "Weapon_LRM_LRM10_2-LongFire": [1, 1],
            "Weapon_LRM_LRM10_2-Telos": [1, 1],
            "Weapon_LRM_LRM10_2-Zeus": [1, 1],
            "Weapon_LRM_LRM10_3-Zeus": [1, 1],
            "Weapon_LRM_LRM15_0-STOCK": [1, 1],
            "Weapon_LRM_LRM15_1-Delta": [1, 1],
            "Weapon_LRM_LRM15_1-LongFire": [1, 1],
            "Weapon_LRM_LRM15_1-Telos": [1, 1],
            "Weapon_LRM_LRM15_2-Delta": [1, 1],
            "Weapon_LRM_LRM15_2-LongFire": [1, 1],
            "Weapon_LRM_LRM15_2-Telos": [1, 1],
            "Weapon_LRM_LRM15_2-Zeus": [1, 1],
            "Weapon_LRM_LRM15_3-Zeus": [1, 1],
            "Weapon_LRM_LRM20_0-STOCK": [1, 1],
            "Weapon_LRM_LRM20_1-Delta": [1, 1],
            "Weapon_LRM_LRM20_1-LongFire": [1, 1],
            "Weapon_LRM_LRM20_1-Telos": [1, 1],
            "Weapon_LRM_LRM20_2-Delta": [1, 1],
            "Weapon_LRM_LRM20_2-LongFire": [1, 1],
            "Weapon_LRM_LRM20_2-Telos": [1, 1],
            "Weapon_LRM_LRM20_2-Zeus": [1, 1],
            "Weapon_LRM_LRM20_3-Zeus": [1, 1],
        },
        "TBOLT": {
            "Weapon_LRM_Thunderbolt5": [1, 1],
            "Weapon_LRM_Thunderbolt10": [1, 1],
            "Weapon_LRM_Thunderbolt15": [1, 1],
            "Weapon_LRM_Thunderbolt20": [1, 1],
        },
        "Artillery": {
            "Weapon_Mortar4": [1, 1],
            "Weapon_Mortar6": [1, 1],
            "Weapon_Mortar8": [1, 1],
            "Weapon_Autocannon_LONGTOM": [1, 1],
            "Weapon_Autocannon_SNIPER": [1, 1],
            "Weapon_Autocannon_THUMPER": [1, 1]
        },
        "Flamer": {
            "Weapon_Flamer_Flamer_0-STOCK": [1, 1],
            "Weapon_Flamer_Flamer_1-Hotshot": [1, 1],
            "Weapon_Flamer_Flamer_2-Olympus": [1, 1],
            "Weapon_Flamer_Flamer_SPECIAL-Victoria": [1, 1],
        },
        "Support": {
            "Weapon_Laser_AMS": [1, 1],
            "Weapon_AMS": [1, 1],
            "Weapon_TAG_Standard_0-STOCK": [1, 1],
            "Weapon_TAG_Standard_1-Mendham": [1, 1],
            "Weapon_TAG_Standard_2-Ceres_Arms": [1, 1],
            "Weapon_Narc_Standard_0-STOCK": [1, 1],
            "Weapon_Narc_Standard_1-Ceres_Arms": [1, 1],
            "Weapon_Narc_Standard_2-Kali_Yama": [1, 1],
        },
    },
    "AmmunitionBox": {
        "Ammo_Common": {
            "Ammo_AmmunitionBox_Generic_MRM": [1, 1],
            "Ammo_AmmunitionBox_Generic_AC2": [1, 1],
            "Ammo_AmmunitionBox_Generic_AC5": [1, 1],
            "Ammo_AmmunitionBox_Generic_AC10": [1, 1],
            "Ammo_AmmunitionBox_Generic_AC20": [1, 1],
            "Ammo_AmmunitionBox_Generic_Flamer": [1, 1],
            "Ammo_AmmunitionBox_Generic_GAUSS": [1, 1],
            "Ammo_AmmunitionBox_Generic_Narc": [1, 1],
            "Ammo_AmmunitionBox_Generic_SRM": [1, 1]
        },
        "Ammo_CommonII": {
            "Ammo_AmmunitionBox_MachineGun": [1, 1],
            "Ammo_AmmunitionBox_AMS": [1, 1],
            "Ammo_AmmunitionBox_Generic_GAUSS": [1, 1],
            "Ammo_AmmunitionBox_Generic_LB2X": [1, 1],
            "Ammo_AmmunitionBox_Generic_LB5X": [1, 1],
            "Ammo_AmmunitionBox_Generic_LB10X": [1, 1],
            "Ammo_AmmunitionBox_Generic_LB20X": [1, 1],
            "Ammo_AmmunitionBox_Generic_LBX10": [1, 1],
            "Ammo_AmmunitionBox_Generic_LBX20": [1, 1],
            "Ammo_AmmunitionBox_Generic_LRM": [1, 1]

        },
        "Ammo_Uncommon": {
            "Ammo_AmmunitionBox_HVAC2": [1, 1],
            "Ammo_AmmunitionBox_HVAC5": [1, 1],
            "Ammo_AmmunitionBox_HVAC10": [1, 1],
            "Ammo_AmmunitionBox_HVAC20": [1, 1],
            "Ammo_AmmunitionBox_TBOLT5": [1, 1],
            "Ammo_AmmunitionBox_TBOLT10": [1, 1],
            "Ammo_AmmunitionBox_TBOLT15": [1, 1],
            "Ammo_AmmunitionBox_TBOLT20": [1, 1],
            "Ammo_AmmunitionBox_Thumper": [1, 1],
            "Ammo_AmmunitionBox_Generic_UAC2": [1, 1],
            "Ammo_AmmunitionBox_Generic_UAC5": [1, 1],
            "Ammo_AmmunitionBox_Generic_UAC10": [1, 1],
            "Ammo_AmmunitionBox_Generic_UAC20": [1, 1],
            "Ammo_AmmunitionBox_ArrowIV": [1, 1]
        },

        "Ammo_Rare": {
            "Ammo_AmmunitionBox_SBGauss": [1, 1],
        },
        "Ammo_Special": {},
    },
    "Mech": {
        "Mechs": {
            "Davion_Light_Mechs": {},
            "Davion_Medium_Mechs": {},
            "Davion_Heavy_Mechs": {},
            "ComStar_Light_Mechs": {},
            "ComStar_Medium_Mechs": {},
            "ComStar_Heavy_Mechs": {},
            "Kurita_Light_Mechs": {},
            "Kurita_Medium_Mechs": {},
            "Kurita_Heavy_Mechs": {},
            "Liao_Light_Mechs": {},
            "Liao_Medium_Mechs": {},
            "Liao_Heavy_Mechs": {},
            "Steiner_Light_Mechs": {},
            "Steiner_Medium_Mechs": {},
            "Steiner_Heavy_Mechs": {},
            "Periphery_Light_Mechs": {},
            "Periphery_Medium_Mechs": {},
            "Periphery_Heavy_Mechs": {},
            "InnerSphere_Light_Mechs": {},
            "InnerSphere_Medium_Mechs": {},
            "InnerSphere_Heavy_Mechs": {},
            "Clan_Light_Mechs": {},
            "Clan_Medium_Mechs": {},
            "Clan_Heavy_Mechs": {},
        },
    },
    "Vehicle": {
        "ComStar_Light_Tanks": {},
        "ComStar_Medium_Tanks": {},
        "ComStar_Heavy_Tanks": {},
        "Kurita_Light_Tanks": {},
        "Kurita_Medium_Tanks": {},
        "Kurita_Heavy_Tanks": {},
        "Liao_Light_Tanks": {},
        "Liao_Medium_Tanks": {},
        "Liao_Heavy_Tanks": {},
        "Steiner_Light_Tanks": {},
        "Steiner_Medium_Tanks": {},
        "Steiner_Heavy_Tanks": {},
        "Periphery_Light_Tanks": {},
        "Periphery_Medium_Tanks": {},
        "Periphery_Heavy_Tanks": {},
        "InnerSphere_Light_Tanks": {},
        "InnerSphere_Medium_Tanks": {},
        "InnerSphere_Heavy_Tanks": {},
        "Clan_Light_Tanks": {},
        "Clan_Medium_Tanks": {},
        "Clan_Heavy_Tanks": {},
    },
    "MechPart": {
        "Davion_Light_Mech_Parts": {},
        "Davion_Medium_Mech_Parts": {},
        "Davion_Heavy_Mech_Parts": {},
        "ComStar_Light_Mech_Parts": {},
        "ComStar_Medium_Mech_Parts": {},
        "ComStar_Heavy_Mech_Parts": {},
        "Kurita_Light_Mech_Parts": {},
        "Kurita_Medium_Mech_Parts": {},
        "Kurita_Heavy_Mech_Parts": {},
        "Liao_Light_Mech_Parts": {},
        "Liao_Medium_Mech_Parts": {},
        "Liao_Heavy_Mech_Parts": {},
        "Steiner_Light_Mech_Parts": {},
        "Steiner_Medium_Mech_Parts": {},
        "Steiner_Heavy_Mech_Parts": {},
        "Periphery_Light_Mech_Parts": {},
        "Periphery_Medium_Mech_Parts": {},
        "Periphery_Heavy_Mech_Parts": {},
        "InnerSphere_Light_Mech_Parts": {},
        "InnerSphere_Medium_Mech_Parts": {},
        "InnerSphere_Heavy_Mech_Parts": {},
        "Clan_Light_Mech_Parts": {},
        "Clan_Medium_Mech_Parts": {},
        "Clan_Heavy_Mech_Parts": {},
    },
    "VehiclePart": {
        "ComStar_Light_Tank_Parts": {},
        "ComStar_Medium_Tank_Parts": {},
        "ComStar_Heavy_Tank_Parts": {},
        "Kurita_Light_Tank_Parts": {},
        "Kurita_Medium_Tank_Parts": {},
        "Kurita_Heavy_Tank_Parts": {},
        "Liao_Light_Tank_Parts": {},
        "Liao_Medium_Tank_Parts": {},
        "Liao_Heavy_Tank_Parts": {},
        "Steiner_Light_Tank_Parts": {},
        "Steiner_Medium_Tank_Parts": {},
        "Steiner_Heavy_Tank_Parts": {},
        "Periphery_Light_Tank_Parts": {},
        "Periphery_Medium_Tank_Parts": {},
        "Periphery_Heavy_Tank_Parts": {},
        "InnerSphere_Light_Tank_Parts": {},
        "InnerSphere_Medium_Tank_Parts": {},
        "InnerSphere_Heavy_Tank_Parts": {},
        "Clan_Light_Tank_Parts": {},
        "Clan_Medium_Tank_Parts": {},
        "Clan_Heavy_Tank_Parts": {}
    }
}
# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the folder name to create
new_folder = "Output"

# Create the full path for the new folder
output_directory = os.path.join(script_dir, new_folder)

# Create the folder
os.makedirs(output_directory, exist_ok=True)

for main_category, subcategories in categories.items():
    for subcategory, values in subcategories.items():
        file_path = f"{output_directory}/GN_{subcategory}.csv"
        with open(file_path, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([f"GN_{subcategory}", '', '', ''])
            if isinstance(values, dict):
                for item, value in values.items():
                    if isinstance(value, dict):
                        value = list(value.values())  # Use values of the inner dictionary
                    elif isinstance(value, set):
                        value = list(value)  # Convert set to list
                    csvwriter.writerow([item, f"{main_category}"] + value)
            else:
                for item in values:
                    csvwriter.writerow([item, f"{main_category}", '', ''])