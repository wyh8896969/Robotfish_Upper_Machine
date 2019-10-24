; Auto-generated. Do not edit!


(cl:in-package msg-msg)


;//! \htmlinclude MotionControl.msg.html

(cl:defclass <MotionControl> (roslisp-msg-protocol:ros-message)
  ((motion
    :reader motion
    :initarg :motion
    :type cl:string
    :initform ""))
)

(cl:defclass MotionControl (<MotionControl>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MotionControl>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MotionControl)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name msg-msg:<MotionControl> is deprecated: use msg-msg:MotionControl instead.")))

(cl:ensure-generic-function 'motion-val :lambda-list '(m))
(cl:defmethod motion-val ((m <MotionControl>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader msg-msg:motion-val is deprecated.  Use msg-msg:motion instead.")
  (motion m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MotionControl>) ostream)
  "Serializes a message object of type '<MotionControl>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'motion))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'motion))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MotionControl>) istream)
  "Deserializes a message object of type '<MotionControl>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'motion) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'motion) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MotionControl>)))
  "Returns string type for a message object of type '<MotionControl>"
  "msg/MotionControl")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MotionControl)))
  "Returns string type for a message object of type 'MotionControl"
  "msg/MotionControl")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MotionControl>)))
  "Returns md5sum for a message object of type '<MotionControl>"
  "56c5b2babfc4b27e5a596091bb964bc2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MotionControl)))
  "Returns md5sum for a message object of type 'MotionControl"
  "56c5b2babfc4b27e5a596091bb964bc2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MotionControl>)))
  "Returns full string definition for message of type '<MotionControl>"
  (cl:format cl:nil "string motion~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MotionControl)))
  "Returns full string definition for message of type 'MotionControl"
  (cl:format cl:nil "string motion~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MotionControl>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'motion))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MotionControl>))
  "Converts a ROS message object to a list"
  (cl:list 'MotionControl
    (cl:cons ':motion (motion msg))
))
