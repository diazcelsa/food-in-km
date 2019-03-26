import React from 'react'
import { Input } from 'semantic-ui-react'
import { connect } from 'react-redux'
import * as a from '../actions';

const InputNameComponent = ({onChange}) => (
    <Input
        id='input-name'
        placeholder='Enter Name'
        onChange={onChange}
    />
)


const InputNameContainer = connect(
    (state, ownProps) => ({
    }),
    (dispatch, ownProps) => ({
        onChange: (event, {value}) => dispatch(a.inputName(value))
    })
)(InputNameComponent)

export default InputNameContainer

