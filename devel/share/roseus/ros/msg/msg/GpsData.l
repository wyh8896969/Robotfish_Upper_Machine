;; Auto-generated. Do not edit!


(when (boundp 'msg::GpsData)
  (if (not (find-package "MSG"))
    (make-package "MSG"))
  (shadow 'GpsData (find-package "MSG")))
(unless (find-package "MSG::GPSDATA")
  (make-package "MSG::GPSDATA"))

(in-package "ROS")
;;//! \htmlinclude GpsData.msg.html


(defclass msg::GpsData
  :super ros::object
  :slots (_velocity _lat _lon _height ))

(defmethod msg::GpsData
  (:init
   (&key
    ((:velocity __velocity) 0.0)
    ((:lat __lat) 0.0)
    ((:lon __lon) 0.0)
    ((:height __height) 0.0)
    )
   (send-super :init)
   (setq _velocity (float __velocity))
   (setq _lat (float __lat))
   (setq _lon (float __lon))
   (setq _height (float __height))
   self)
  (:velocity
   (&optional __velocity)
   (if __velocity (setq _velocity __velocity)) _velocity)
  (:lat
   (&optional __lat)
   (if __lat (setq _lat __lat)) _lat)
  (:lon
   (&optional __lon)
   (if __lon (setq _lon __lon)) _lon)
  (:height
   (&optional __height)
   (if __height (setq _height __height)) _height)
  (:serialization-length
   ()
   (+
    ;; float32 _velocity
    4
    ;; float32 _lat
    4
    ;; float32 _lon
    4
    ;; float32 _height
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _velocity
       (sys::poke _velocity (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _lat
       (sys::poke _lat (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _lon
       (sys::poke _lon (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _height
       (sys::poke _height (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _velocity
     (setq _velocity (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _lat
     (setq _lat (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _lon
     (setq _lon (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _height
     (setq _height (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get msg::GpsData :md5sum-) "ba3cc63050e4d95f5191738e220625ed")
(setf (get msg::GpsData :datatype-) "msg/GpsData")
(setf (get msg::GpsData :definition-)
      "float32 velocity
float32 lat
float32 lon
float32 height
")



(provide :msg/GpsData "ba3cc63050e4d95f5191738e220625ed")


