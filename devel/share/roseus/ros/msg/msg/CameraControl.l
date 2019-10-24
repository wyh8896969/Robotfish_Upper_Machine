;; Auto-generated. Do not edit!


(when (boundp 'msg::CameraControl)
  (if (not (find-package "MSG"))
    (make-package "MSG"))
  (shadow 'CameraControl (find-package "MSG")))
(unless (find-package "MSG::CAMERACONTROL")
  (make-package "MSG::CAMERACONTROL"))

(in-package "ROS")
;;//! \htmlinclude CameraControl.msg.html


(defclass msg::CameraControl
  :super ros::object
  :slots (_mode ))

(defmethod msg::CameraControl
  (:init
   (&key
    ((:mode __mode) "")
    )
   (send-super :init)
   (setq _mode (string __mode))
   self)
  (:mode
   (&optional __mode)
   (if __mode (setq _mode __mode)) _mode)
  (:serialization-length
   ()
   (+
    ;; string _mode
    4 (length _mode)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _mode
       (write-long (length _mode) s) (princ _mode s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _mode
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _mode (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get msg::CameraControl :md5sum-) "e84dc3ad5dc323bb64f0aca01c2d1eef")
(setf (get msg::CameraControl :datatype-) "msg/CameraControl")
(setf (get msg::CameraControl :definition-)
      "string mode
")



(provide :msg/CameraControl "e84dc3ad5dc323bb64f0aca01c2d1eef")


