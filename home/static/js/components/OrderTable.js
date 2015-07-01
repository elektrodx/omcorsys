/*
 * Modules Dependencies
 */

import React from 'react';
import OrderHead from './OrderHead';
import OrderList from './OrderList';


export default class OrderTable extends React.Component {
 	render(){
 		return <table className="order-table">
 			<OrderHead/>
 			<OrderList orders={this.props.orders}/>	
 		</table>
 	}
 }