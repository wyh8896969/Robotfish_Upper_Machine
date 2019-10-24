;; Auto-generated. Do not edit!


(when (boundp 'msg::PecControl)
  (if (not (find-package "MSG"))
    (make-package "MSG"))
  (shadow 'PecControl (find-package "MSG")))
(unless (find-package "MSG::PECCONTROL")
  (make-package "MSG::PECCONTROL"))

(in-package "ROS")
;;//! \htmlinclude PecControl.msg.html


(defclass msg::PecControl
  :super ros::object
  :slots (_mode ))

(defmethod msg::PecControl
  (:init
   (&key
    ((:mode __mode) 0)
    )
   (send-super :init)
   (setq _mode (round __mode))
   self)
  (:mode
   (&optional __mode)
   (if __mode (setq _mode __mode)) _mode)
  (:serialization-length
   ()
   (+
    ;; int32 _mode
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _mode
       (write-long _mode s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _mode
     (setq _mode (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get msg::PecControl :md5sum-) "ff63f6ea3c3e9b7504b2cb3ee0a09d92")
(setf (get msg::PecControl :datatype-) "msg/PecControl")
(setf (get msg::PecControl :definition-)
      "int32 mode
")



(provide :msg/PecControl "ff63f6ea3c3e9b7504b2cb3ee0a09d92")


