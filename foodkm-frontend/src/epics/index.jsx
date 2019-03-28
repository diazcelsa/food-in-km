import { ajax } from 'rxjs/ajax';
import { combineEpics, ofType } from 'redux-observable';
import { of } from 'rxjs';
import { map, catchError, concatMap, tap, withLatestFrom, filter, debounceTime, startWith } from 'rxjs/operators';
import * as a from '../actions';
import { BACKEND_URL } from '../config'


const makeURL = (action, state) => {
    const {lat, lon} = state.location;
    const query = action.query;
    return (BACKEND_URL + '/search?query=' + query + '&lat=' + lat + '&lon=' + lon)
}


const productSearchEpic = (action$, state$) => (
    action$.pipe(
        ofType('PRODUCTS_SEARCH'),
        debounceTime(1000),
        withLatestFrom(state$),
        map(([action, state]) => ({url: makeURL(action, state)})),
        tap(console.log, console.log),
        concatMap(
            (action) => (
                ajax.get(action.url).pipe(
                    tap(console.log, console.log),
                    map(response => a.updateProducts(response.response.results, response.response.suggest))
                )
            )
        ),
        catchError(val => of(a.error('Could not update products.', val)))
    )
);


const makeLocationURL = (action, state) => {
    const query = action.query;
    return (BACKEND_URL + '/location?query=' + query)
}


const locationSearchEpic = (action$, state$) => (
    action$.pipe(
        ofType('LOCATION_SEARCH'),
        filter(({query}) => (query.length == 5)),
        debounceTime(1000),
        withLatestFrom(state$),
        map(([action, state]) => ({url: makeLocationURL(action, state)})),
        tap(console.log, console.log),
        concatMap(
            (action) => (
                ajax.get(action.url).pipe(
                    tap(console.log, console.log),
                    filter(response => (response.response.lat)),
                    map(response => a.locationUpdate(response.response))
                )
            )
        ),
        catchError(val => of(a.error('Could not update products.', val)))
    )
);


const epics = combineEpics(
    productSearchEpic,
    locationSearchEpic
);

export default epics;
