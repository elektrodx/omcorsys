/*
 * Modules Dependencies
 */

import React from 'react';

export default class OrderList extends React.Component {
	render() {
	 return <tr className = 'order-list'>
			<td>{this.props.orders.order_id}</td>
			<td>{this.props.orders.customer}</td>
			<td>{this.props.orders.date}</td>
			<td>{this.props.orders.date_due}</td>
			<td>{this.props.orders.weight}</td>
			<td>{this.props.orders.amount} $</td>
			<td>{this.props.orders.state}</td> 
		</tr>
	}
}