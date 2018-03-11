'use strict';

// Declare app level module which depends on views, and components
angular.module('myApp', [
  'ngRoute',
  'firebase',
  'myApp.data',
  'myApp.dashboard',
  'myApp.tasks',
  'myApp.projects',
  'myApp.departments',
  'myApp.employees',
  'firebase'
]).
config(['$locationProvider', '$routeProvider', function($locationProvider, $routeProvider) {
  $locationProvider.hashPrefix('!');

  $routeProvider.otherwise({redirectTo: '/'});
}]);
