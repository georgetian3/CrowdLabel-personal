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

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', process.cwd()+'/src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require(process.cwd()+'/src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.CrowdLabelApi);
  }
}(this, function(expect, CrowdLabelApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new CrowdLabelApi.DefaultApi();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('DefaultApi', function() {
    describe('availabilityAvailabilityPost', function() {
      it('should call availabilityAvailabilityPost successfully', function(done) {
        //uncomment below and update the code to test availabilityAvailabilityPost
        //instance.availabilityAvailabilityPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('downloadResultsDownloadResultsGet', function() {
      it('should call downloadResultsDownloadResultsGet successfully', function(done) {
        //uncomment below and update the code to test downloadResultsDownloadResultsGet
        //instance.downloadResultsDownloadResultsGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('faviconFaviconIcoGet', function() {
      it('should call faviconFaviconIcoGet successfully', function(done) {
        //uncomment below and update the code to test faviconFaviconIcoGet
        //instance.faviconFaviconIcoGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getPagePageGet', function() {
      it('should call getPagePageGet successfully', function(done) {
        //uncomment below and update the code to test getPagePageGet
        //instance.getPagePageGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('helloHelloPost', function() {
      it('should call helloHelloPost successfully', function(done) {
        //uncomment below and update the code to test helloHelloPost
        //instance.helloHelloPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('indexGet', function() {
      it('should call indexGet successfully', function(done) {
        //uncomment below and update the code to test indexGet
        //instance.indexGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('loginLoginPost', function() {
      it('should call loginLoginPost successfully', function(done) {
        //uncomment below and update the code to test loginLoginPost
        //instance.loginLoginPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readItemsItemsGet', function() {
      it('should call readItemsItemsGet successfully', function(done) {
        //uncomment below and update the code to test readItemsItemsGet
        //instance.readItemsItemsGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readUsersMeUsersMeGet', function() {
      it('should call readUsersMeUsersMeGet successfully', function(done) {
        //uncomment below and update the code to test readUsersMeUsersMeGet
        //instance.readUsersMeUsersMeGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('registerRegisterPost', function() {
      it('should call registerRegisterPost successfully', function(done) {
        //uncomment below and update the code to test registerRegisterPost
        //instance.registerRegisterPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('uploadTaskUploadTaskPost', function() {
      it('should call uploadTaskUploadTaskPost successfully', function(done) {
        //uncomment below and update the code to test uploadTaskUploadTaskPost
        //instance.uploadTaskUploadTaskPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('wrappertaskTaskIdGet', function() {
      it('should call wrappertaskTaskIdGet successfully', function(done) {
        //uncomment below and update the code to test wrappertaskTaskIdGet
        //instance.wrappertaskTaskIdGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('wrappertasksTasksGet', function() {
      it('should call wrappertasksTasksGet successfully', function(done) {
        //uncomment below and update the code to test wrappertasksTasksGet
        //instance.wrappertasksTasksGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('wrapperuserUserUsernameGet', function() {
      it('should call wrapperuserUserUsernameGet successfully', function(done) {
        //uncomment below and update the code to test wrapperuserUserUsernameGet
        //instance.wrapperuserUserUsernameGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
