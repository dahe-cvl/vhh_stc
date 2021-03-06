from vhh_stc.STC import STC
import os

config_file = "./config/config_vhh_test.yaml"
stc_instance = STC(config_file)

if(stc_instance.config_instance.debug_flag == True):
    print("DEBUG MODE activated!")
    sbd_results_file = stc_instance.config_instance.sbd_results_path
    shots_np = stc_instance.loadSbdResults(sbd_results_file)
    max_recall_id = int(shots_np[0][0].split('.')[0])
    stc_instance.runOnSingleVideo(shots_per_vid_np=shots_np, max_recall_id=max_recall_id)
else:
    results_path = "/data/share/cvl_vhh_software/release_v1_2_1/vhh_core/results/stc/final_results/"
    dst_path = "/data/ext/VHH/datasets/vhh_mmsi_core_results_v1_2_1_keyframes/"
    video_path = "/data/share/cvl_vhh_software/release_v1_2_1/vhh_core/videos"

    results_file_list = os.listdir(results_path)
    print(results_file_list)

    for file in results_file_list:
        shots_np = stc_instance.loadStcResults(results_path + file)
        stc_instance.extract_frames_per_shot(shots_per_vid_np=shots_np,
                                             number_of_frames=1,
                                             dst_path=dst_path,
                                             video_path=video_path
                                             )

