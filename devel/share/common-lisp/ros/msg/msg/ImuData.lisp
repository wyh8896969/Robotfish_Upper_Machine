; Auto-generated. Do not edit!


(cl:in-package msg-msg)


;//! \htmlinclude ImuData.msg.html

(cl:defclass <ImuData> (roslisp-msg-protocol:ros-message)
  ((acc
    :reader acc
    :initarg :acc
    :type cl:string
    :initform "")
   (ang
    :reader ang
    :initarg :ang
    :type cl:string
    :initform "")
   (gyro
    :reader gyro
    :initarg :gyro
    :type cl:string
    :initform "")
   (mag
    :reader mag
    :initarg :mag
    :type cl:string
    :initform ""))
)

(cl:defclass ImuData (<ImuData>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ImuData>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ImuData)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name msg-msg:<ImuData> is deprecated: use msg-msg:ImuData instead.")))

(cl:ensure-generic-function 'acc-val :lambda-list '(m))
(cl:defmethod acc-val ((m <ImuData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader msg-msg:acc-val is deprecated.  Use msg-msg:acc instead.")
  (acc m))

(cl:ensure-generic-function 'ang-val :lambda-list '(m))
(cl:defmethod ang-val ((m <ImuData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader msg-msg:ang-val is deprecated.  Use msg-msg:ang instead.")
  (ang m))

(cl:ensure-generic-function 'gyro-val :lambda-list '(m))
(cl:defmethod gyro-val ((m <ImuData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader msg-msg:gyro-val is deprecated.  Use msg-msg:gyro instead.")
  (gyro m))

(cl:ensure-generic-function 'mag-val :lambda-list '(m))
(cl:defmethod mag-val ((m <ImuData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader msg-msg:mag-val is deprecated.  Use msg-msg:mag instead.")
  (mag m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ImuData>) ostream)
  "Serializes a message object of type '<ImuData>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'acc))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'acc))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'ang))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'ang))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'gyro))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'gyro))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'mag))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'mag))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ImuData>) istream)
  "Deserializes a message object of type '<ImuData>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'acc) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'acc) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'ang) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'ang) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'gyro) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'gyro) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'mag) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'mag) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ImuData>)))
  "Returns string type for a message object of type '<ImuData>"
  "msg/ImuData")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ImuData)))
  "Returns string type for a message object of type 'ImuData"
  "msg/ImuData")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ImuData>)))
  "Returns md5sum for a message object of type '<ImuData>"
  "c17d5a58c7143586f17ab489cda5df38")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ImuData)))
  "Returns md5sum for a message object of type 'ImuData"
  "c17d5a58c7143586f17ab489cda5df38")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ImuData>)))
  "Returns full string definition for message of type '<ImuData>"
  (cl:format cl:nil "string acc~%string ang~%string gyro~%string mag~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ImuData)))
  "Returns full string definition for message of type 'ImuData"
  (cl:format cl:nil "string acc~%string ang~%string gyro~%string mag~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ImuData>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'acc))
     4 (cl:length (cl:slot-value msg 'ang))
     4 (cl:length (cl:slot-value msg 'gyro))
     4 (cl:length (cl:slot-value msg 'mag))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ImuData>))
  "Converts a ROS message object to a list"
  (cl:list 'ImuData
    (cl:cons ':acc (acc msg))
    (cl:cons ':ang (ang msg))
    (cl:cons ':gyro (gyro msg))
    (cl:cons ':mag (mag msg))
))
