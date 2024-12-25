import zarr

# Zarrファイルを読み込む
zarr_file = zarr.open("data/replay_buffer.zarr", mode="r")

# actionデータを確認
print(zarr_file['data'].tree())
for i in range(0, 100, 10):
    print(f"action: {zarr_file['data']['action'][i]}")
    print(f"pose: {zarr_file['data']['robot_eef_pose'][i]}\n")

# # robot_eef_poseデータを確認
# print("\nrobot_eef_pose dataset:")
# print(f"Shape: {zarr_file['robot_eef_pose'].shape}")
# print(f"Dtype: {zarr_file['robot_eef_pose'].dtype}")
# print("Sample data:")
# print(zarr_file['robot_eef_pose'][:5])  # 最初の5行を表示