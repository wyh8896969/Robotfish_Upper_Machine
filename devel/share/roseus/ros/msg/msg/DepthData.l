;; Auto-generated. Do not edit!


(when (boundp 'msg::DepthData)
  (if (not (find-package "MSG"))
    (make-package "MSG"))
  (shadow 'DepthData (find-package "MSG")))
(unless (find-package "MSG::DEPTHDATA")
  (make-package "MSG::DEPTHDATA"))

(in-package "ROS")
;;//! \htmlinclude DepthData.msg.html


(defclass msg::DepthData
  :super ros::object
  :slots (_depth _pressure _temp ))

(defmethod msg::DepthData
  (:init
   (&key
    ((:depth __depth) 0.0)
    ((:pressure __pressure) 0.0)
    ((:temp __temp) 0.0)
    )
   (send-super :init)
   (setq _depth (float __depth))
   (setq _pressure (float __pressure))
   (setq _temp (float __temp))
   self)
  (:depth
   (&optional __depth)
   (if __depth (setq _depth __depth)) _depth)
  (:pressure
   (&optional __pressure)
   (if __pressure (setq _pressure __pressure)) _pressure)
  (:temp
   (&optional __temp)
   (if __temp (setq _temp __temp)) _temp)
  (:serialization-length
   ()
   (+
    ;; float32 _depth
    4
    ;; float32 _pressure
    4
    ;; float32 _temp
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _depth
       (sys::poke _depth (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _pressure
       (sys::poke _pressure (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _temp
       (sys::poke _temp (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _depth
     (setq _depth (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _pressure
     (setq _pressure (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _temp
     (setq _temp (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get msg::DepthData :md5sum-) "c6ad25ee4a8b5281bb4c431c5fdf360e")
(setf (get msg::DepthData :datatype-) "msg/DepthData")
(setf (get msg::DepthData :definition-)
      "float32 depth
float32 pressure
float32 temp
")



(provide :msg/DepthData "c6ad25ee4a8b5281bb4c431c5fdf360e")


