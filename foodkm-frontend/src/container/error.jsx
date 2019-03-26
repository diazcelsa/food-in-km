import React from 'react';
import _ from 'lodash';
import { Message } from 'semantic-ui-react';
import { connect } from 'react-redux';
import * as a from '../actions';


const ErrorComponent = ({message, trace, onDismiss, error_id}) => (
  <Message error={true} onDismiss={onDismiss} key={'error-message-' + error_id}>
    <Message.Header>{message}</Message.Header>
    {trace.message}
  </Message>
)

const ErrorsComponent = ({errors, onDismiss}) => (
    _.map(errors, ({message, trace}, idx) => (
        <ErrorComponent message={message} trace={trace} onDismiss={onDismiss} error_id={idx} key={'error-comp-' + idx} />
    ))
)

const ErrorsContainer = connect(
    (state, ownProps) => ({
        errors: state.errors
    }),
    (dispatch, ownProps) => ({
        onDismiss: (event, {value}) => dispatch(a.acknowledgeError(value))
    })
)(ErrorsComponent)

export default ErrorsContainer
