/*
 * Modules Dependencies
 */

import React from 'react';
import OrderHead from './OrderHead';
import OrderList from './OrderList';
import jquery from 'jquery';

var $ = require('jquery');





export default class OrderTable extends React.Component {
	constructor(props){
		super(props)
		this.state = { orders: [] }
	}

	componentDidMount() {
	    $.get('http://localhost:8000/api/orders/?format=json', (result) => {
      var orders = result.results;
      this.setState({ orders: orders })
      }.bind(this));
  	}
 	render(){
 		return <table className="order-table">
 			<OrderHead/>
 			<OrderList key={this.state.orders.id} orders={this.state.orders}/>
 		</table>
 	}
 }

