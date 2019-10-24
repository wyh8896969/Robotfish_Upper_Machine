;; Auto-generated. Do not edit!


(when (boundp 'msg::SensorsData)
  (if (not (find-package "MSG"))
    (make-package "MSG"))
  (shadow 'SensorsData (find-package "MSG")))
(unless (find-package "MSG::SENSORSDATA")
  (make-package "MSG::SENSORSDATA"))

(in-package "ROS")
;;//! \htmlinclude SensorsData.msg.html


(defclass msg::SensorsData
  :super ros::object
  :slots (_data ))

(defmethod msg::SensorsData
  (:init
   (&key
    ((:data __data) "")
    )
   (send-super :init)
   (setq _data (string __data))
   self)
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:serialization-length
   ()
   (+
    ;; string _data
    4 (length _data)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _data
       (write-long (length _data) s) (princ _data s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _data
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _data (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get msg::SensorsData :md5sum-) "992ce8a1687cec8c8bd883ec73ca41d1")
(setf (get msg::SensorsData :datatype-) "msg/SensorsData")
(setf (get msg::SensorsData :definition-)
      "string data
")



(provide :msg/SensorsData "992ce8a1687cec8c8bd883ec73ca41d1")


