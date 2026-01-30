### 📚 Table of Contents

* [Dataset Description](#dataset-description)
* [Dataset Parts](#dataset-parts)
* [Data Structure and File Organization](#data-structure-and-file-organization)
* [Downloads](#downloads)
* [Examples and Teasers](#examples-and-teasers)
* [Acknowledgement](#acknowledgement)

# Örebro 4D-radar SLAM Challenge Data [UNDER CONSTRUCTION]



## Dataset description
![Viking hill in Orebro](media/husky_in_snow.jpg)
*The recorded track captures the [Enbuskabacken](https://www.lansstyrelsen.se/orebro/besoksmal/kulturmiljoer/enbuskabacken.html) and the neighboring university campus in Örebro.*

This dataset serves as the training and competition track in the 4D-radar SLAM challenge organized by the [Radar in Robotics: New Frontiers](https://sites.google.com/view/radar-robotics/home) workshop at the [ICRA 2026](https://2026.ieee-icra.org/workshops-and-tutorials/) conference.
The dataset consists of two trajectories driven with a Husky robot through a forested area (approx. 200x200m) and the neighbouring Örebro university campus.
It was recorded in January 2026. The terrain in the forrested area is uneven because it used to serve as a burial ground during the Viking Age (550-1050 AD). Even the campus portion of the trajectory involves climbing up some inclined paths and sloped terrain.
The dataset includes a liDAR, three 4D radar sensors, a GNSS reference, an RGB camera and an IMU.
In the training run, all data are provided. In the competition run, only the radars and IMU are available.

![Training run reference lidar map](media/map_training.jpg)
*The reference lidar map for the training run, created using the GLIM SLAM package.*

---

## Dataset Parts
### Public Training Part

* **01_campus_training_localized** (2257s)
 A 1.8km-long trajectory that covers both the natural and urban environment at the campus. Its shape was chosen as to offer several opportunities for loop closure.

### Hidden Testing Part

* **02_campus_eval_filtered** (3813s)
 A 2.6km-long track that covers the same environment. It also allows several loop closures. From this run, we provide only the radar and IMU data. The competition SLAM systems must be able to localize and map with these modalities.
 
---

## Data Structure and File Organization

```
grass_track_training/
├── calibration
│   ├── extrinsics
│   │   └── frames.pdf
│   └── intrinsics
│       └── hugin_radar_startup_params.txt
├── LICENSE.txt
├── readme.txt
├── reference
│   ├── reference.txt
│   └── supplementary
│       ├── reference_train_bagfile.bag
│       ├── reference_train_gps_rtk_in_robot_time.csv
│       └── source_rtk_solution_from_Emlid_RTKLIB
│           ├── gps_filtered_high_accuracy.pos
│           ├── gsp_original_post_fix_including_bad_sections.pos
│           └── train_robot_time_to_gps_time.csv
├── sensors
│   ├── grass_track_training__2025-06-12-22-12-48_0.bag
│   ├── ...
│   └── grass_track_training__2025-06-12-23-38-13_31.bag
└── tracks
    └── default.txt
```

* `grass_track_training__<sequence time and number>.bag` → Raw sensory data and static transforms.
* `reference/` → Folder containing reference RTK trajectories.
* `calibration/extrinsics/` → Transformations between sensor frames.
* `calibration/instrinsics/` → Intrinsic parameters for the camera and radar settings.

### Sensors
The dataset provides sensor measurements from these sensors:

* Sensrad Hugin A3-Sample (solid-state 4D radar)
  * Please note that the Hugin A3-Sample radar used in our dataset is an early demo model not with the same performance as the forthcoming production-ready model.
* Ouster OS0-32 (3D lidar)
  * This sensor is available for tuning and verification of your SLAM solution, but not available in the competition runs (i.e., the topic with point clouds will not be published in the Docker environment).  
* IDS Imaging uEye camera (2056x1542px)
* Xsens MTi-30 (IMU)
* Emlid Reach RS2+ (RTK-GNSS receiver pair)

### Reference Contents

The dataset contains a `reference/` subdirectory with:

* `reference_train_bagfile.bag`: Reference GNSS RTK localization synchrized with the robot time, saved as a bag file.
* `reference.txt`: The GNSS RTK expressed in the UTM coordinates, with time stamps from the robot. Format: **timestamp[s], northing[m], easting[m], elevation, qx, qy, qz, qw**. Note that the quarternion is always identity.
* `reference_train_gps_rtk_in_robot_time.csv`: Contains the same information as `reference.txt`, but expressed in latitude and longitude. Format: **secs, nsecs, latitude, longitude, elevation**.
* `gps_filtered_high_accuracy.pos`: RTK solution used to generate the reference samples for the files above. It does not contain sections with too few sattelites. Note that the displayed time is the GPS time (no time zone, no step seconds).
* `gsp_original_post_fix_including_bad_sections.pos`: Complete RTK solution, wih all samples including the noisy ones.
* `train_robot_time_to_gps_time.csv`: Conversion from the robot time to the time indicated by the GNSS. The robot was no exactly synchronized with the GNSS, there is approx. 0.6s offset. This file can be used to match those times. Format: **robot secs, robot nsecs, gnss secs, gnss nsecs** 

---

## Downloads

* [All training data](https://cloud.oru.se/s/6jFmgbrsq7Amrde) (32 GB in total)

---

## Examples and Teasers

![Viking hill in Orebro](media/husky_sm.jpg)

*Recorded in June, the grass was tall enough to often obscure the robot sensors.*

![Viking hill in Orebro](media/vegetation_sm.jpg)

*The robot was intentionally driven through bushes and over uneven terrain.*

### Video Teasers

[![Watch the video](https://img.youtube.com/vi/WGpa2mYYAf0/default.jpg)](https://youtu.be/WGpa2mYYAf0)
[![Watch the video](https://img.youtube.com/vi/Ioj59OIlEVM/default.jpg)](https://youtu.be/Ioj59OIlEVM)

## Acknowledgement

The camera stream in this dataset was anonymized using [EgoBlur](https://github.com/facebookresearch/EgoBlur) 
* Raina, N., Somasundaram, G., Zheng, K., Miglani, S., Saarinen, S., Meissner, J., Schwesinger, M., Pesqueira, L., Prasad, I., Miller, E., Gupta, P., Yan, M., Newcombe, R., Ren, C., & Parkhi, O. M. (2023). EgoBlur: Responsible Innovation in Aria. arXiv preprint [arXiv:2308.13093](https://arxiv.org/abs/2308.13093).

The work on this dataset was supported by the European Union's Horizon Europe Framework Programme under the RaCOON project (ID: 101106906).

![Funded by EU](media/EN_FundedbytheEU_RGB_POS.png)


