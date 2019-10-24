;; Auto-generated. Do not edit!


(when (boundp 'msg::MotionControl)
  (if (not (find-package "MSG"))
    (make-package "MSG"))
  (shadow 'MotionControl (find-package "MSG")))
(unless (find-package "MSG::MOTIONCONTROL")
  (make-package "MSG::MOTIONCONTROL"))

(in-package "ROS")
;;//! \htmlinclude MotionControl.msg.html


(defclass msg::MotionControl
  :super ros::object
  :slots (_motion ))

(defmethod msg::MotionControl
  (:init
   (&key
    ((:motion __motion) "")
    )
   (send-super :init)
   (setq _motion (string __motion))
   self)
  (:motion
   (&optional __motion)
   (if __motion (setq _motion __motion)) _motion)
  (:serialization-length
   ()
   (+
    ;; string _motion
    4 (length _motion)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _motion
       (write-long (length _motion) s) (princ _motion s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _motion
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _motion (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get msg::MotionControl :md5sum-) "56c5b2babfc4b27e5a596091bb964bc2")
(setf (get msg::MotionControl :datatype-) "msg/MotionControl")
(setf (get msg::MotionControl :definition-)
      "string motion
")



(provide :msg/MotionControl "56c5b2babfc4b27e5a596091bb964bc2")


