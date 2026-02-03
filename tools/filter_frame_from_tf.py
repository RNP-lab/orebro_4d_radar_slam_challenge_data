import rosbag2_py
from rclpy.serialization import deserialize_message, serialize_message
from rosidl_runtime_py.utilities import get_message
from tf2_msgs.msg import TFMessage

# This is how we removed the odom frame from the competition track, for example:
input_bag = "./02_campus_eval_2026_01_20_14h_41m_29s"
output_bag = "./02_campus_eval_no_odom_frame"
excluded_frame = "odom"

reader = rosbag2_py.SequentialReader()
storage_options = rosbag2_py.StorageOptions(uri=input_bag, storage_id="mcap")
converter_options = rosbag2_py.ConverterOptions(input_serialization_format="cdr", output_serialization_format="cdr")
reader.open(storage_options, converter_options)

writer = rosbag2_py.SequentialWriter()
writer.open(
    rosbag2_py.StorageOptions(uri=output_bag, storage_id="mcap"),
    converter_options,
)

topic_types = reader.get_all_topics_and_types()
for topic in topic_types:
    writer.create_topic(topic)

while reader.has_next():
    topic, data, t = reader.read_next()

    if topic == "/tf":
        msg_type = get_message("tf2_msgs/msg/TFMessage")
        msg = deserialize_message(data, msg_type)

        # Keep only transforms not involving excluded_frame
        filtered_transforms = [
            tr for tr in msg.transforms
            if tr.header.frame_id != excluded_frame and tr.child_frame_id != excluded_frame
        ]

        if not filtered_transforms:
            continue  # skip message entirely

        msg.transforms = filtered_transforms
        data = serialize_message(msg)

    writer.write(topic, data, t)

print(f"Filtered bag saved to: {output_bag}")
