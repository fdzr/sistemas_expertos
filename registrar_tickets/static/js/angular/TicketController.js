'use strict';

var app = angular.module('ticketApp', []);

app.config(['$httpProvider', function($httpProvider){
	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

}]);

app.config(function($interpolateProvider){
	$interpolateProvider.startSymbol('[[');
	$interpolateProvider.endSymbol(']]');

});


app.controller('TicketController', function($scope, $http){

	$http.get('http://127.0.0.1:8000/api/tickets').then(function(response){
		$scope.tickets = response.data;
	});
});

angular.module('ticketApp').config(['$qProvider', function($qProvider){
   $qProvider.errorOnUnhandledRejections(false);

}]);

app.controller('AddTicketController', function($scope, $http){

	$scope.save = function(){
	$http({
		method: 'POST',
		url: 'http://127.0.0.1:8000/api/tickets/create/',
		data: {'titulo': $scope.titulo,
			   'descripcion': $scope.descripcion,
			   'estado': $scope.estado},

		}).then(function(){
			window.location = "http://127.0.0.1:8000/index";
		});
	};

	
	

});