; Auto-generated. Do not edit!


(cl:in-package msg-msg)


;//! \htmlinclude CameraControl.msg.html

(cl:defclass <CameraControl> (roslisp-msg-protocol:ros-message)
  ((mode
    :reader mode
    :initarg :mode
    :type cl:string
    :initform ""))
)

(cl:defclass CameraControl (<CameraControl>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CameraControl>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CameraControl)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name msg-msg:<CameraControl> is deprecated: use msg-msg:CameraControl instead.")))

(cl:ensure-generic-function 'mode-val :lambda-list '(m))
(cl:defmethod mode-val ((m <CameraControl>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader msg-msg:mode-val is deprecated.  Use msg-msg:mode instead.")
  (mode m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CameraControl>) ostream)
  "Serializes a message object of type '<CameraControl>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'mode))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'mode))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CameraControl>) istream)
  "Deserializes a message object of type '<CameraControl>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'mode) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'mode) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CameraControl>)))
  "Returns string type for a message object of type '<CameraControl>"
  "msg/CameraControl")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CameraControl)))
  "Returns string type for a message object of type 'CameraControl"
  "msg/CameraControl")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CameraControl>)))
  "Returns md5sum for a message object of type '<CameraControl>"
  "e84dc3ad5dc323bb64f0aca01c2d1eef")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CameraControl)))
  "Returns md5sum for a message object of type 'CameraControl"
  "e84dc3ad5dc323bb64f0aca01c2d1eef")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CameraControl>)))
  "Returns full string definition for message of type '<CameraControl>"
  (cl:format cl:nil "string mode~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CameraControl)))
  "Returns full string definition for message of type 'CameraControl"
  (cl:format cl:nil "string mode~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CameraControl>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'mode))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CameraControl>))
  "Converts a ROS message object to a list"
  (cl:list 'CameraControl
    (cl:cons ':mode (mode msg))
))
