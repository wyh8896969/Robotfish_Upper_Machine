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

class ImuData {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.acc = null;
      this.ang = null;
      this.gyro = null;
      this.mag = null;
    }
    else {
      if (initObj.hasOwnProperty('acc')) {
        this.acc = initObj.acc
      }
      else {
        this.acc = '';
      }
      if (initObj.hasOwnProperty('ang')) {
        this.ang = initObj.ang
      }
      else {
        this.ang = '';
      }
      if (initObj.hasOwnProperty('gyro')) {
        this.gyro = initObj.gyro
      }
      else {
        this.gyro = '';
      }
      if (initObj.hasOwnProperty('mag')) {
        this.mag = initObj.mag
      }
      else {
        this.mag = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ImuData
    // Serialize message field [acc]
    bufferOffset = _serializer.string(obj.acc, buffer, bufferOffset);
    // Serialize message field [ang]
    bufferOffset = _serializer.string(obj.ang, buffer, bufferOffset);
    // Serialize message field [gyro]
    bufferOffset = _serializer.string(obj.gyro, buffer, bufferOffset);
    // Serialize message field [mag]
    bufferOffset = _serializer.string(obj.mag, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ImuData
    let len;
    let data = new ImuData(null);
    // Deserialize message field [acc]
    data.acc = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [ang]
    data.ang = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [gyro]
    data.gyro = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [mag]
    data.mag = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.acc.length;
    length += object.ang.length;
    length += object.gyro.length;
    length += object.mag.length;
    return length + 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'msg/ImuData';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c17d5a58c7143586f17ab489cda5df38';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string acc
    string ang
    string gyro
    string mag
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ImuData(null);
    if (msg.acc !== undefined) {
      resolved.acc = msg.acc;
    }
    else {
      resolved.acc = ''
    }

    if (msg.ang !== undefined) {
      resolved.ang = msg.ang;
    }
    else {
      resolved.ang = ''
    }

    if (msg.gyro !== undefined) {
      resolved.gyro = msg.gyro;
    }
    else {
      resolved.gyro = ''
    }

    if (msg.mag !== undefined) {
      resolved.mag = msg.mag;
    }
    else {
      resolved.mag = ''
    }

    return resolved;
    }
};

module.exports = ImuData;
