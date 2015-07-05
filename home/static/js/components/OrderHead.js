/*
 * Modules Dependencies
 */

import React from 'react';

export default class OrderHead extends React.Component {
	render(){
		return <tr className = 'order-head'>
			<th> Pedido N </th>
			<th className='order-customer'> Cliente </th>
			<th className='order-date'> Fecha </th>
			<th> Limite de Entrega </th>
			<th> Peso </th>
			<th> Monto </th>
			<th> Estado </th> 
		</tr>
	}
}