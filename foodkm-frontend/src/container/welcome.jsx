import React from 'react'
import { Input } from 'semantic-ui-react'
import { connect } from 'react-redux'
import * as a from '../actions';

const WelcomeComponent = ({name}) => (
    <div id='welcome-message'>Hello {name}!</div>
)

const WelcomeContainer = connect(
    (state, ownProps) => ({
        name: state.name
    }),
    (dispatch, ownProps) => ({
    })
)(WelcomeComponent)

export default WelcomeContainer
