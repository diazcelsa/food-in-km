import { ajax } from 'rxjs/ajax';
import { combineEpics, ofType } from 'redux-observable';
import { of } from 'rxjs';
import { map, catchError, concatMap, tap, withLatestFrom } from 'rxjs/operators';
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
        withLatestFrom(state$),
        map(([action, state]) => ({url: makeURL(action, state)})),
        tap(console.log, console.log),
        concatMap(
            (action) => (
                ajax.get(action.url).pipe(
                    tap(console.log, console.log),
                    map(response => a.updateProducts(response.response.results))
                )
            )
        ),
        catchError(val => of(a.error('Could not update products.', val)))
    )
);




const epics = combineEpics(
    productSearchEpic,

);

export default epics;
