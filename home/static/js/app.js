/*
 * Modules Dependiencies
 */

import React from 'react';
import OrderTable from './components/OrderTable';

let orders = {
order_id: (1),
customer: 'jgonzales',
date: '25/06/2015',
date_due: '30/07/2015',
weight: '5',
amount: '55',
state: 'pedido',
}

React.render(<OrderTable orders={orders}/>, document.getElementById('container'));