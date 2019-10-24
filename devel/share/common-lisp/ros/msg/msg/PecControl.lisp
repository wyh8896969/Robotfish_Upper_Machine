; Auto-generated. Do not edit!


(cl:in-package msg-msg)


;//! \htmlinclude PecControl.msg.html

(cl:defclass <PecControl> (roslisp-msg-protocol:ros-message)
  ((mode
    :reader mode
    :initarg :mode
    :type cl:integer
    :initform 0))
)

(cl:defclass PecControl (<PecControl>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PecControl>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PecControl)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name msg-msg:<PecControl> is deprecated: use msg-msg:PecControl instead.")))

(cl:ensure-generic-function 'mode-val :lambda-list '(m))
(cl:defmethod mode-val ((m <PecControl>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader msg-msg:mode-val is deprecated.  Use msg-msg:mode instead.")
  (mode m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PecControl>) ostream)
  "Serializes a message object of type '<PecControl>"
  (cl:let* ((signed (cl:slot-value msg 'mode)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PecControl>) istream)
  "Deserializes a message object of type '<PecControl>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'mode) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PecControl>)))
  "Returns string type for a message object of type '<PecControl>"
  "msg/PecControl")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PecControl)))
  "Returns string type for a message object of type 'PecControl"
  "msg/PecControl")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PecControl>)))
  "Returns md5sum for a message object of type '<PecControl>"
  "ff63f6ea3c3e9b7504b2cb3ee0a09d92")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PecControl)))
  "Returns md5sum for a message object of type 'PecControl"
  "ff63f6ea3c3e9b7504b2cb3ee0a09d92")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PecControl>)))
  "Returns full string definition for message of type '<PecControl>"
  (cl:format cl:nil "int32 mode~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PecControl)))
  "Returns full string definition for message of type 'PecControl"
  (cl:format cl:nil "int32 mode~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PecControl>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PecControl>))
  "Converts a ROS message object to a list"
  (cl:list 'PecControl
    (cl:cons ':mode (mode msg))
))
