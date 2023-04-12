
"use strict";

let node_disable_contact_points_tracking = require('./node_disable_contact_points_tracking.js')
let node_get_id = require('./node_get_id.js')
let gps_decimal_degrees_to_degrees_minutes_seconds = require('./gps_decimal_degrees_to_degrees_minutes_seconds.js')
let node_move_viewpoint = require('./node_move_viewpoint.js')
let node_get_static_balance = require('./node_get_static_balance.js')
let set_float_array = require('./set_float_array.js')
let field_get_name = require('./field_get_name.js')
let lidar_get_frequency_info = require('./lidar_get_frequency_info.js')
let field_remove_node = require('./field_remove_node.js')
let field_get_count = require('./field_get_count.js')
let display_get_info = require('./display_get_info.js')
let node_set_velocity = require('./node_set_velocity.js')
let node_disable_pose_tracking = require('./node_disable_pose_tracking.js')
let display_image_paste = require('./display_image_paste.js')
let field_get_bool = require('./field_get_bool.js')
let speaker_play_sound = require('./speaker_play_sound.js')
let automobile_get_dimensions = require('./automobile_get_dimensions.js')
let node_enable_pose_tracking = require('./node_enable_pose_tracking.js')
let node_reset_functions = require('./node_reset_functions.js')
let display_set_font = require('./display_set_font.js')
let skin_set_bone_orientation = require('./skin_set_bone_orientation.js')
let field_get_node = require('./field_get_node.js')
let range_finder_get_info = require('./range_finder_get_info.js')
let display_draw_oval = require('./display_draw_oval.js')
let node_is_proto = require('./node_is_proto.js')
let node_get_orientation = require('./node_get_orientation.js')
let node_get_status = require('./node_get_status.js')
let field_get_type = require('./field_get_type.js')
let field_enable_sf_tracking = require('./field_enable_sf_tracking.js')
let supervisor_get_from_def = require('./supervisor_get_from_def.js')
let field_set_vec2f = require('./field_set_vec2f.js')
let node_get_string = require('./node_get_string.js')
let display_draw_rectangle = require('./display_draw_rectangle.js')
let get_float = require('./get_float.js')
let field_set_float = require('./field_set_float.js')
let get_int = require('./get_int.js')
let node_get_center_of_mass = require('./node_get_center_of_mass.js')
let node_add_force_with_offset = require('./node_add_force_with_offset.js')
let display_image_save = require('./display_image_save.js')
let speaker_speak = require('./speaker_speak.js')
let node_get_parent_node = require('./node_get_parent_node.js')
let display_image_copy = require('./display_image_copy.js')
let lidar_get_layer_range_image = require('./lidar_get_layer_range_image.js')
let supervisor_get_from_id = require('./supervisor_get_from_id.js')
let motor_set_control_pid = require('./motor_set_control_pid.js')
let get_urdf = require('./get_urdf.js')
let node_get_type = require('./node_get_type.js')
let skin_set_bone_position = require('./skin_set_bone_position.js')
let node_get_field = require('./node_get_field.js')
let robot_wait_for_user_input_event = require('./robot_wait_for_user_input_event.js')
let speaker_is_sound_playing = require('./speaker_is_sound_playing.js')
let supervisor_set_label = require('./supervisor_set_label.js')
let supervisor_movie_stop_recording = require('./supervisor_movie_stop_recording.js')
let set_float = require('./set_float.js')
let field_get_int32 = require('./field_get_int32.js')
let get_float_array = require('./get_float_array.js')
let field_set_rotation = require('./field_set_rotation.js')
let display_draw_line = require('./display_draw_line.js')
let camera_get_zoom_info = require('./camera_get_zoom_info.js')
let supervisor_movie_start_recording = require('./supervisor_movie_start_recording.js')
let node_get_position = require('./node_get_position.js')
let field_set_string = require('./field_set_string.js')
let skin_get_bone_name = require('./skin_get_bone_name.js')
let display_draw_polygon = require('./display_draw_polygon.js')
let display_image_delete = require('./display_image_delete.js')
let robot_set_mode = require('./robot_set_mode.js')
let mouse_get_state = require('./mouse_get_state.js')
let camera_get_focus_info = require('./camera_get_focus_info.js')
let set_int = require('./set_int.js')
let field_remove = require('./field_remove.js')
let supervisor_get_from_string = require('./supervisor_get_from_string.js')
let skin_get_bone_orientation = require('./skin_get_bone_orientation.js')
let display_draw_text = require('./display_draw_text.js')
let node_remove = require('./node_remove.js')
let display_image_new = require('./display_image_new.js')
let lidar_get_layer_point_cloud = require('./lidar_get_layer_point_cloud.js')
let get_string = require('./get_string.js')
let node_get_number_of_fields = require('./node_get_number_of_fields.js')
let field_disable_sf_tracking = require('./field_disable_sf_tracking.js')
let supervisor_virtual_reality_headset_get_orientation = require('./supervisor_virtual_reality_headset_get_orientation.js')
let field_get_string = require('./field_get_string.js')
let set_string = require('./set_string.js')
let display_draw_pixel = require('./display_draw_pixel.js')
let get_uint64 = require('./get_uint64.js')
let supervisor_virtual_reality_headset_get_position = require('./supervisor_virtual_reality_headset_get_position.js')
let node_set_visibility = require('./node_set_visibility.js')
let field_set_color = require('./field_set_color.js')
let display_image_load = require('./display_image_load.js')
let node_enable_contact_points_tracking = require('./node_enable_contact_points_tracking.js')
let field_set_bool = require('./field_set_bool.js')
let field_get_vec3f = require('./field_get_vec3f.js')
let field_get_vec2f = require('./field_get_vec2f.js')
let field_get_float = require('./field_get_float.js')
let pen_set_ink_color = require('./pen_set_ink_color.js')
let node_set_string = require('./node_set_string.js')
let save_image = require('./save_image.js')
let robot_get_device_list = require('./robot_get_device_list.js')
let node_get_name = require('./node_get_name.js')
let node_set_joint_position = require('./node_set_joint_position.js')
let node_get_velocity = require('./node_get_velocity.js')
let set_bool = require('./set_bool.js')
let field_import_node_from_string = require('./field_import_node_from_string.js')
let get_bool = require('./get_bool.js')
let field_get_color = require('./field_get_color.js')
let camera_get_info = require('./camera_get_info.js')
let node_add_force_or_torque = require('./node_add_force_or_torque.js')
let field_get_rotation = require('./field_get_rotation.js')
let node_get_pose = require('./node_get_pose.js')
let field_set_int32 = require('./field_set_int32.js')
let skin_get_bone_position = require('./skin_get_bone_position.js')
let lidar_get_info = require('./lidar_get_info.js')
let node_get_field_by_index = require('./node_get_field_by_index.js')
let field_set_vec3f = require('./field_set_vec3f.js')
let node_get_contact_points = require('./node_get_contact_points.js')
let receiver_get_emitter_direction = require('./receiver_get_emitter_direction.js')

module.exports = {
  node_disable_contact_points_tracking: node_disable_contact_points_tracking,
  node_get_id: node_get_id,
  gps_decimal_degrees_to_degrees_minutes_seconds: gps_decimal_degrees_to_degrees_minutes_seconds,
  node_move_viewpoint: node_move_viewpoint,
  node_get_static_balance: node_get_static_balance,
  set_float_array: set_float_array,
  field_get_name: field_get_name,
  lidar_get_frequency_info: lidar_get_frequency_info,
  field_remove_node: field_remove_node,
  field_get_count: field_get_count,
  display_get_info: display_get_info,
  node_set_velocity: node_set_velocity,
  node_disable_pose_tracking: node_disable_pose_tracking,
  display_image_paste: display_image_paste,
  field_get_bool: field_get_bool,
  speaker_play_sound: speaker_play_sound,
  automobile_get_dimensions: automobile_get_dimensions,
  node_enable_pose_tracking: node_enable_pose_tracking,
  node_reset_functions: node_reset_functions,
  display_set_font: display_set_font,
  skin_set_bone_orientation: skin_set_bone_orientation,
  field_get_node: field_get_node,
  range_finder_get_info: range_finder_get_info,
  display_draw_oval: display_draw_oval,
  node_is_proto: node_is_proto,
  node_get_orientation: node_get_orientation,
  node_get_status: node_get_status,
  field_get_type: field_get_type,
  field_enable_sf_tracking: field_enable_sf_tracking,
  supervisor_get_from_def: supervisor_get_from_def,
  field_set_vec2f: field_set_vec2f,
  node_get_string: node_get_string,
  display_draw_rectangle: display_draw_rectangle,
  get_float: get_float,
  field_set_float: field_set_float,
  get_int: get_int,
  node_get_center_of_mass: node_get_center_of_mass,
  node_add_force_with_offset: node_add_force_with_offset,
  display_image_save: display_image_save,
  speaker_speak: speaker_speak,
  node_get_parent_node: node_get_parent_node,
  display_image_copy: display_image_copy,
  lidar_get_layer_range_image: lidar_get_layer_range_image,
  supervisor_get_from_id: supervisor_get_from_id,
  motor_set_control_pid: motor_set_control_pid,
  get_urdf: get_urdf,
  node_get_type: node_get_type,
  skin_set_bone_position: skin_set_bone_position,
  node_get_field: node_get_field,
  robot_wait_for_user_input_event: robot_wait_for_user_input_event,
  speaker_is_sound_playing: speaker_is_sound_playing,
  supervisor_set_label: supervisor_set_label,
  supervisor_movie_stop_recording: supervisor_movie_stop_recording,
  set_float: set_float,
  field_get_int32: field_get_int32,
  get_float_array: get_float_array,
  field_set_rotation: field_set_rotation,
  display_draw_line: display_draw_line,
  camera_get_zoom_info: camera_get_zoom_info,
  supervisor_movie_start_recording: supervisor_movie_start_recording,
  node_get_position: node_get_position,
  field_set_string: field_set_string,
  skin_get_bone_name: skin_get_bone_name,
  display_draw_polygon: display_draw_polygon,
  display_image_delete: display_image_delete,
  robot_set_mode: robot_set_mode,
  mouse_get_state: mouse_get_state,
  camera_get_focus_info: camera_get_focus_info,
  set_int: set_int,
  field_remove: field_remove,
  supervisor_get_from_string: supervisor_get_from_string,
  skin_get_bone_orientation: skin_get_bone_orientation,
  display_draw_text: display_draw_text,
  node_remove: node_remove,
  display_image_new: display_image_new,
  lidar_get_layer_point_cloud: lidar_get_layer_point_cloud,
  get_string: get_string,
  node_get_number_of_fields: node_get_number_of_fields,
  field_disable_sf_tracking: field_disable_sf_tracking,
  supervisor_virtual_reality_headset_get_orientation: supervisor_virtual_reality_headset_get_orientation,
  field_get_string: field_get_string,
  set_string: set_string,
  display_draw_pixel: display_draw_pixel,
  get_uint64: get_uint64,
  supervisor_virtual_reality_headset_get_position: supervisor_virtual_reality_headset_get_position,
  node_set_visibility: node_set_visibility,
  field_set_color: field_set_color,
  display_image_load: display_image_load,
  node_enable_contact_points_tracking: node_enable_contact_points_tracking,
  field_set_bool: field_set_bool,
  field_get_vec3f: field_get_vec3f,
  field_get_vec2f: field_get_vec2f,
  field_get_float: field_get_float,
  pen_set_ink_color: pen_set_ink_color,
  node_set_string: node_set_string,
  save_image: save_image,
  robot_get_device_list: robot_get_device_list,
  node_get_name: node_get_name,
  node_set_joint_position: node_set_joint_position,
  node_get_velocity: node_get_velocity,
  set_bool: set_bool,
  field_import_node_from_string: field_import_node_from_string,
  get_bool: get_bool,
  field_get_color: field_get_color,
  camera_get_info: camera_get_info,
  node_add_force_or_torque: node_add_force_or_torque,
  field_get_rotation: field_get_rotation,
  node_get_pose: node_get_pose,
  field_set_int32: field_set_int32,
  skin_get_bone_position: skin_get_bone_position,
  lidar_get_info: lidar_get_info,
  node_get_field_by_index: node_get_field_by_index,
  field_set_vec3f: field_set_vec3f,
  node_get_contact_points: node_get_contact_points,
  receiver_get_emitter_direction: receiver_get_emitter_direction,
};
