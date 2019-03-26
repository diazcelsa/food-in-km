import { ajax } from 'rxjs/ajax';
import { combineEpics, ofType } from 'redux-observable';
import { of } from 'rxjs';
import { map, catchError, concatMap, tap } from 'rxjs/operators';
import * as a from '../actions';
import { BACKEND_URL } from '../config'


const makeUpperRequest = (action) => (
    {data: {name: action.name}}
)


const nameInputEpic = (action$, state$) => (
    action$.pipe(
        ofType('NAME_INPUT'),
        map((action) => ({request: makeUpperRequest(action), url: BACKEND_URL + '/upper'})),
        concatMap(
            (action) => (
                ajax.post(action.url, action.request, {'Content-Type': 'application/json', 'Cache-Control': 'no-cache'}).pipe(
                    tap(console.log, console.log),
                    map(response => a.changeName(response.response.data.name))
                )
            )
        ),
        catchError(val => of(a.error('Could not upper name.', val)))
    )
);


const epics = combineEpics(
    nameInputEpic
);

export default epics;
