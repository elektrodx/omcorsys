import jquery from 'jquery';

var $ = require('jquery');

export default class OrderApi {
    constructor () {
        this.baseUrl = 'http://localhost:8000/orders/?format=json'

    }

    findOrder (title) {
        let url = `${this.baseUrl}`
        return Promise.resolve($.get(url))
    }
}
