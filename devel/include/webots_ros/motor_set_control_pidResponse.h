// Generated by gencpp from file webots_ros/motor_set_control_pidResponse.msg
// DO NOT EDIT!


#ifndef WEBOTS_ROS_MESSAGE_MOTOR_SET_CONTROL_PIDRESPONSE_H
#define WEBOTS_ROS_MESSAGE_MOTOR_SET_CONTROL_PIDRESPONSE_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace webots_ros
{
template <class ContainerAllocator>
struct motor_set_control_pidResponse_
{
  typedef motor_set_control_pidResponse_<ContainerAllocator> Type;

  motor_set_control_pidResponse_()
    : success(0)  {
    }
  motor_set_control_pidResponse_(const ContainerAllocator& _alloc)
    : success(0)  {
  (void)_alloc;
    }



   typedef int8_t _success_type;
  _success_type success;





  typedef boost::shared_ptr< ::webots_ros::motor_set_control_pidResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::webots_ros::motor_set_control_pidResponse_<ContainerAllocator> const> ConstPtr;

}; // struct motor_set_control_pidResponse_

typedef ::webots_ros::motor_set_control_pidResponse_<std::allocator<void> > motor_set_control_pidResponse;

typedef boost::shared_ptr< ::webots_ros::motor_set_control_pidResponse > motor_set_control_pidResponsePtr;
typedef boost::shared_ptr< ::webots_ros::motor_set_control_pidResponse const> motor_set_control_pidResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::webots_ros::motor_set_control_pidResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::webots_ros::motor_set_control_pidResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::webots_ros::motor_set_control_pidResponse_<ContainerAllocator1> & lhs, const ::webots_ros::motor_set_control_pidResponse_<ContainerAllocator2> & rhs)
{
  return lhs.success == rhs.success;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::webots_ros::motor_set_control_pidResponse_<ContainerAllocator1> & lhs, const ::webots_ros::motor_set_control_pidResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace webots_ros

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::webots_ros::motor_set_control_pidResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::webots_ros::motor_set_control_pidResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::webots_ros::motor_set_control_pidResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::webots_ros::motor_set_control_pidResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::webots_ros::motor_set_control_pidResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::webots_ros::motor_set_control_pidResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::webots_ros::motor_set_control_pidResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "0b13460cb14006d3852674b4c614f25f";
  }

  static const char* value(const ::webots_ros::motor_set_control_pidResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x0b13460cb14006d3ULL;
  static const uint64_t static_value2 = 0x852674b4c614f25fULL;
};

template<class ContainerAllocator>
struct DataType< ::webots_ros::motor_set_control_pidResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "webots_ros/motor_set_control_pidResponse";
  }

  static const char* value(const ::webots_ros::motor_set_control_pidResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::webots_ros::motor_set_control_pidResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int8 success\n"
"\n"
;
  }

  static const char* value(const ::webots_ros::motor_set_control_pidResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::webots_ros::motor_set_control_pidResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.success);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct motor_set_control_pidResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::webots_ros::motor_set_control_pidResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::webots_ros::motor_set_control_pidResponse_<ContainerAllocator>& v)
  {
    s << indent << "success: ";
    Printer<int8_t>::stream(s, indent + "  ", v.success);
  }
};

} // namespace message_operations
} // namespace ros

#endif // WEBOTS_ROS_MESSAGE_MOTOR_SET_CONTROL_PIDRESPONSE_H
