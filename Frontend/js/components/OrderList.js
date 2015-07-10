/*
 * Modules Dependencies
 */

import React from 'react';
import OrderMap from './OrderMap'


export default class OrderList extends React.Component {
	render() {
	return <table>
	{
	this.props.orders.map((order) => {
		return <OrderMap key={this.props.key} order={order}/>	
	})	
	}	
	</table>
}	
}