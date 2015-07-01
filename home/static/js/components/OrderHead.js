/*
 * Modules Dependencies
 */

import React from 'react';

export default class OrderHead extends React.Component {
	render(){
		return <tr className = 'order-head'>
			<th> Pedido N </th>
			<th> Cliente </th>
			<th> Fecha </th>
			<th> Limite de Entrega </th>
			<th> Peso </th>
			<th> Monto </th>
			<th> Estado </th> 
		</tr>
	}
}