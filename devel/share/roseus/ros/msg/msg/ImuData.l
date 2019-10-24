;; Auto-generated. Do not edit!


(when (boundp 'msg::ImuData)
  (if (not (find-package "MSG"))
    (make-package "MSG"))
  (shadow 'ImuData (find-package "MSG")))
(unless (find-package "MSG::IMUDATA")
  (make-package "MSG::IMUDATA"))

(in-package "ROS")
;;//! \htmlinclude ImuData.msg.html


(defclass msg::ImuData
  :super ros::object
  :slots (_acc _ang _gyro _mag ))

(defmethod msg::ImuData
  (:init
   (&key
    ((:acc __acc) "")
    ((:ang __ang) "")
    ((:gyro __gyro) "")
    ((:mag __mag) "")
    )
   (send-super :init)
   (setq _acc (string __acc))
   (setq _ang (string __ang))
   (setq _gyro (string __gyro))
   (setq _mag (string __mag))
   self)
  (:acc
   (&optional __acc)
   (if __acc (setq _acc __acc)) _acc)
  (:ang
   (&optional __ang)
   (if __ang (setq _ang __ang)) _ang)
  (:gyro
   (&optional __gyro)
   (if __gyro (setq _gyro __gyro)) _gyro)
  (:mag
   (&optional __mag)
   (if __mag (setq _mag __mag)) _mag)
  (:serialization-length
   ()
   (+
    ;; string _acc
    4 (length _acc)
    ;; string _ang
    4 (length _ang)
    ;; string _gyro
    4 (length _gyro)
    ;; string _mag
    4 (length _mag)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _acc
       (write-long (length _acc) s) (princ _acc s)
     ;; string _ang
       (write-long (length _ang) s) (princ _ang s)
     ;; string _gyro
       (write-long (length _gyro) s) (princ _gyro s)
     ;; string _mag
       (write-long (length _mag) s) (princ _mag s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _acc
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _acc (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _ang
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _ang (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _gyro
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _gyro (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _mag
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _mag (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get msg::ImuData :md5sum-) "c17d5a58c7143586f17ab489cda5df38")
(setf (get msg::ImuData :datatype-) "msg/ImuData")
(setf (get msg::ImuData :definition-)
      "string acc
string ang
string gyro
string mag
")



(provide :msg/ImuData "c17d5a58c7143586f17ab489cda5df38")


