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

class DepthData {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.depth = null;
      this.pressure = null;
      this.temp = null;
    }
    else {
      if (initObj.hasOwnProperty('depth')) {
        this.depth = initObj.depth
      }
      else {
        this.depth = 0.0;
      }
      if (initObj.hasOwnProperty('pressure')) {
        this.pressure = initObj.pressure
      }
      else {
        this.pressure = 0.0;
      }
      if (initObj.hasOwnProperty('temp')) {
        this.temp = initObj.temp
      }
      else {
        this.temp = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type DepthData
    // Serialize message field [depth]
    bufferOffset = _serializer.float32(obj.depth, buffer, bufferOffset);
    // Serialize message field [pressure]
    bufferOffset = _serializer.float32(obj.pressure, buffer, bufferOffset);
    // Serialize message field [temp]
    bufferOffset = _serializer.float32(obj.temp, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type DepthData
    let len;
    let data = new DepthData(null);
    // Deserialize message field [depth]
    data.depth = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [pressure]
    data.pressure = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [temp]
    data.temp = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'msg/DepthData';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c6ad25ee4a8b5281bb4c431c5fdf360e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 depth
    float32 pressure
    float32 temp
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new DepthData(null);
    if (msg.depth !== undefined) {
      resolved.depth = msg.depth;
    }
    else {
      resolved.depth = 0.0
    }

    if (msg.pressure !== undefined) {
      resolved.pressure = msg.pressure;
    }
    else {
      resolved.pressure = 0.0
    }

    if (msg.temp !== undefined) {
      resolved.temp = msg.temp;
    }
    else {
      resolved.temp = 0.0
    }

    return resolved;
    }
};

module.exports = DepthData;
