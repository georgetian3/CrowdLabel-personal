/**
 * CrowdLabelAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The JWT model module.
 * @module model/JWT
 * @version 0.1.0
 */
class JWT {
    /**
     * Constructs a new <code>JWT</code>.
     * @alias module:model/JWT
     * @param jwt {String} 
     */
    constructor(jwt) { 
        
        JWT.initialize(this, jwt);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, jwt) { 
        obj['jwt'] = jwt;
    }

    /**
     * Constructs a <code>JWT</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/JWT} obj Optional instance to populate.
     * @return {module:model/JWT} The populated <code>JWT</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new JWT();

            if (data.hasOwnProperty('jwt')) {
                obj['jwt'] = ApiClient.convertToType(data['jwt'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>JWT</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>JWT</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of JWT.RequiredProperties) {
            if (!data[property]) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['jwt'] && !(typeof data['jwt'] === 'string' || data['jwt'] instanceof String)) {
            throw new Error("Expected the field `jwt` to be a primitive type in the JSON string but got " + data['jwt']);
        }

        return true;
    }


}

JWT.RequiredProperties = ["jwt"];

/**
 * @member {String} jwt
 */
JWT.prototype['jwt'] = undefined;






export default JWT;

