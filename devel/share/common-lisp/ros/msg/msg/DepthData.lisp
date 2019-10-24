; Auto-generated. Do not edit!


(cl:in-package msg-msg)


;//! \htmlinclude DepthData.msg.html

(cl:defclass <DepthData> (roslisp-msg-protocol:ros-message)
  ((depth
    :reader depth
    :initarg :depth
    :type cl:float
    :initform 0.0)
   (pressure
    :reader pressure
    :initarg :pressure
    :type cl:float
    :initform 0.0)
   (temp
    :reader temp
    :initarg :temp
    :type cl:float
    :initform 0.0))
)

(cl:defclass DepthData (<DepthData>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DepthData>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DepthData)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name msg-msg:<DepthData> is deprecated: use msg-msg:DepthData instead.")))

(cl:ensure-generic-function 'depth-val :lambda-list '(m))
(cl:defmethod depth-val ((m <DepthData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader msg-msg:depth-val is deprecated.  Use msg-msg:depth instead.")
  (depth m))

(cl:ensure-generic-function 'pressure-val :lambda-list '(m))
(cl:defmethod pressure-val ((m <DepthData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader msg-msg:pressure-val is deprecated.  Use msg-msg:pressure instead.")
  (pressure m))

(cl:ensure-generic-function 'temp-val :lambda-list '(m))
(cl:defmethod temp-val ((m <DepthData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader msg-msg:temp-val is deprecated.  Use msg-msg:temp instead.")
  (temp m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DepthData>) ostream)
  "Serializes a message object of type '<DepthData>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'depth))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'pressure))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'temp))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DepthData>) istream)
  "Deserializes a message object of type '<DepthData>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'depth) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'pressure) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'temp) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DepthData>)))
  "Returns string type for a message object of type '<DepthData>"
  "msg/DepthData")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DepthData)))
  "Returns string type for a message object of type 'DepthData"
  "msg/DepthData")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DepthData>)))
  "Returns md5sum for a message object of type '<DepthData>"
  "c6ad25ee4a8b5281bb4c431c5fdf360e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DepthData)))
  "Returns md5sum for a message object of type 'DepthData"
  "c6ad25ee4a8b5281bb4c431c5fdf360e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DepthData>)))
  "Returns full string definition for message of type '<DepthData>"
  (cl:format cl:nil "float32 depth~%float32 pressure~%float32 temp~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DepthData)))
  "Returns full string definition for message of type 'DepthData"
  (cl:format cl:nil "float32 depth~%float32 pressure~%float32 temp~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DepthData>))
  (cl:+ 0
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DepthData>))
  "Converts a ROS message object to a list"
  (cl:list 'DepthData
    (cl:cons ':depth (depth msg))
    (cl:cons ':pressure (pressure msg))
    (cl:cons ':temp (temp msg))
))
