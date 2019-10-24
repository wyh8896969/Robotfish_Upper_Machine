; Auto-generated. Do not edit!


(cl:in-package msg-msg)


;//! \htmlinclude SensorsData.msg.html

(cl:defclass <SensorsData> (roslisp-msg-protocol:ros-message)
  ((data
    :reader data
    :initarg :data
    :type cl:string
    :initform ""))
)

(cl:defclass SensorsData (<SensorsData>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SensorsData>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SensorsData)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name msg-msg:<SensorsData> is deprecated: use msg-msg:SensorsData instead.")))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <SensorsData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader msg-msg:data-val is deprecated.  Use msg-msg:data instead.")
  (data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SensorsData>) ostream)
  "Serializes a message object of type '<SensorsData>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'data))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SensorsData>) istream)
  "Deserializes a message object of type '<SensorsData>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'data) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'data) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SensorsData>)))
  "Returns string type for a message object of type '<SensorsData>"
  "msg/SensorsData")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SensorsData)))
  "Returns string type for a message object of type 'SensorsData"
  "msg/SensorsData")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SensorsData>)))
  "Returns md5sum for a message object of type '<SensorsData>"
  "992ce8a1687cec8c8bd883ec73ca41d1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SensorsData)))
  "Returns md5sum for a message object of type 'SensorsData"
  "992ce8a1687cec8c8bd883ec73ca41d1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SensorsData>)))
  "Returns full string definition for message of type '<SensorsData>"
  (cl:format cl:nil "string data~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SensorsData)))
  "Returns full string definition for message of type 'SensorsData"
  (cl:format cl:nil "string data~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SensorsData>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'data))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SensorsData>))
  "Converts a ROS message object to a list"
  (cl:list 'SensorsData
    (cl:cons ':data (data msg))
))
