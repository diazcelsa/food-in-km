export const changeName = (name) => {
    return {
      type: 'NAME_CHANGE',
      name
    };
}

export const inputName = (name) => {
  return {
    type: 'NAME_INPUT',
    name
  };
}

export const error = (message, trace) => {
  return {
    type: 'ERROR',
    message,
    trace
  };
}


export const acknowledgeError = () => {
  return {
    type: 'ERROR_ACKNOWLEDGED'
  };
}
