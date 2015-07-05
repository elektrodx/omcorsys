/*
 * Modules Dependencies
 */

import React from 'react';


export default class OrderMap extends React.Component {
	
	render() {
		return <tr className = 'order-list'>
				<td className= 'order-id'>{this.props.order.id}</td>
				<td className = 'order-customer'>{this.props.order.customer}</td>
				<td className = 'order-date'>{this.props.order.date}</td>
				<td className = 'order-date_due'>{this.props.order.date_due}</td>
				<td className = 'order-weight'>{this.props.order.weight}</td>
				<td className = 'order-amount'>{this.props.order.amount}</td>
				<td className = 'order-state'>{this.props.order.state}</td>
			</tr>
	}
} 