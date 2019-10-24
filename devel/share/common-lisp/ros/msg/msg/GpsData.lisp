; Auto-generated. Do not edit!


(cl:in-package msg-msg)


;//! \htmlinclude GpsData.msg.html

(cl:defclass <GpsData> (roslisp-msg-protocol:ros-message)
  ((velocity
    :reader velocity
    :initarg :velocity
    :type cl:float
    :initform 0.0)
   (lat
    :reader lat
    :initarg :lat
    :type cl:float
    :initform 0.0)
   (lon
    :reader lon
    :initarg :lon
    :type cl:float
    :initform 0.0)
   (height
    :reader height
    :initarg :height
    :type cl:float
    :initform 0.0))
)

(cl:defclass GpsData (<GpsData>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GpsData>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GpsData)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name msg-msg:<GpsData> is deprecated: use msg-msg:GpsData instead.")))

(cl:ensure-generic-function 'velocity-val :lambda-list '(m))
(cl:defmethod velocity-val ((m <GpsData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader msg-msg:velocity-val is deprecated.  Use msg-msg:velocity instead.")
  (velocity m))

(cl:ensure-generic-function 'lat-val :lambda-list '(m))
(cl:defmethod lat-val ((m <GpsData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader msg-msg:lat-val is deprecated.  Use msg-msg:lat instead.")
  (lat m))

(cl:ensure-generic-function 'lon-val :lambda-list '(m))
(cl:defmethod lon-val ((m <GpsData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader msg-msg:lon-val is deprecated.  Use msg-msg:lon instead.")
  (lon m))

(cl:ensure-generic-function 'height-val :lambda-list '(m))
(cl:defmethod height-val ((m <GpsData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader msg-msg:height-val is deprecated.  Use msg-msg:height instead.")
  (height m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GpsData>) ostream)
  "Serializes a message object of type '<GpsData>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'velocity))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'lat))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'lon))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'height))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GpsData>) istream)
  "Deserializes a message object of type '<GpsData>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'velocity) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'lat) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'lon) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'height) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GpsData>)))
  "Returns string type for a message object of type '<GpsData>"
  "msg/GpsData")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GpsData)))
  "Returns string type for a message object of type 'GpsData"
  "msg/GpsData")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GpsData>)))
  "Returns md5sum for a message object of type '<GpsData>"
  "ba3cc63050e4d95f5191738e220625ed")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GpsData)))
  "Returns md5sum for a message object of type 'GpsData"
  "ba3cc63050e4d95f5191738e220625ed")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GpsData>)))
  "Returns full string definition for message of type '<GpsData>"
  (cl:format cl:nil "float32 velocity~%float32 lat~%float32 lon~%float32 height~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GpsData)))
  "Returns full string definition for message of type 'GpsData"
  (cl:format cl:nil "float32 velocity~%float32 lat~%float32 lon~%float32 height~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GpsData>))
  (cl:+ 0
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GpsData>))
  "Converts a ROS message object to a list"
  (cl:list 'GpsData
    (cl:cons ':velocity (velocity msg))
    (cl:cons ':lat (lat msg))
    (cl:cons ':lon (lon msg))
    (cl:cons ':height (height msg))
))
