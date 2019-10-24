// Auto-generated. Do not edit!

// (in-package msg.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class MotionControl {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.motion = null;
    }
    else {
      if (initObj.hasOwnProperty('motion')) {
        this.motion = initObj.motion
      }
      else {
        this.motion = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MotionControl
    // Serialize message field [motion]
    bufferOffset = _serializer.string(obj.motion, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MotionControl
    let len;
    let data = new MotionControl(null);
    // Deserialize message field [motion]
    data.motion = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.motion.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'msg/MotionControl';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '56c5b2babfc4b27e5a596091bb964bc2';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string motion
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MotionControl(null);
    if (msg.motion !== undefined) {
      resolved.motion = msg.motion;
    }
    else {
      resolved.motion = ''
    }

    return resolved;
    }
};

module.exports = MotionControl;
