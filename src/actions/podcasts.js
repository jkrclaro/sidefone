import axios from '../axios';
import {
    GET_PODCASTS_REQUEST,
    GET_PODCASTS_SUCCESS,
    GET_PODCAST_REQUEST,
    GET_PODCAST_SUCCESS,
    GET_PODCAST_FAILURE,
    SHOW_PLAYER,
    PLAY_EPISODE,
    FETCH_EPISODES_REQUEST,
    FETCH_EPISODES_SUCCESS,
    FETCH_EPISODES_FAILURE,
    PLAY_PLAYER,
    PAUSE_PLAYER,
    SUBSCRIBE_PODCAST_SUCCESS,
    UNSUBSCRIBE_PODCAST_SUCCESS,
    GET_PODCAST_SUBSCRIPTION_REQUEST,
    GET_PODCAST_SUBSCRIPTION_SUCCESS
} from './types';


export const fetchPodcasts = () => async (dispatch) => {
    dispatch({ type: GET_PODCASTS_REQUEST })
    const response = await axios.get('/podplayer/subscriptions');
    dispatch({
        type: GET_PODCASTS_SUCCESS,
        payload: response.data
    });
};

export const fetchEpisodes = (id) => async dispatch => {
    dispatch({ type: FETCH_EPISODES_REQUEST });
    try {
        const response = await axios.get(`/podplayer/podcasts/${id}/episodes/`)
        dispatch({
            type: FETCH_EPISODES_SUCCESS,
            payload: response.data
        })
    } catch(e) {
        dispatch({ type: FETCH_EPISODES_FAILURE, payload: [] })
    }
}

export const fetchPodcast = id => async (dispatch) => {
    dispatch({ type: GET_PODCAST_REQUEST });
    try {
        const response = await axios.get(`/podplayer/podcasts/${id}`);
        dispatch({
            type: GET_PODCAST_SUCCESS,
            payload: response.data
        });
    } catch(error) {
        dispatch({
            type: GET_PODCAST_FAILURE,
            payload: {}
        })
    }
}

export const showPlayer = () => async dispatch => {
    dispatch({
        type: SHOW_PLAYER
    })
}

export const playEpisode = (podcast, episode) => async dispatch => {
    dispatch({
        type: PLAY_EPISODE,
        podcast,
        episode
    })
}

export const playPlayer = () => async dispatch => {
    dispatch({
        type: PLAY_PLAYER
    })
}

export const pausePlayer = () => async dispatch => {
    dispatch({
        type: PAUSE_PLAYER
    })
}

export const subscribePodcast = name => async (dispatch) => {
    const payload = { name }
    await axios.post('/podplayer/podcasts/subscribe', payload);
    dispatch({
        type: SUBSCRIBE_PODCAST_SUCCESS,
        payload: {is_subscribed: true}
    })
}

export const unsubscribePodcast = name => async (dispatch) => {
    const payload = { name }
    await axios.post('/podplayer/podcasts/unsubscribe', payload);
    dispatch({
        type: UNSUBSCRIBE_PODCAST_SUCCESS,
        payload: {is_subscribed: false}
    })
}

export const fetchPodcastsubscription = itunes_id => async (dispatch) => {
    dispatch({ type: GET_PODCAST_SUBSCRIPTION_REQUEST });
    const payload = { itunes_id }
    const response = await axios.post('/podplayer/podcasts/subscription', payload);
    dispatch({
        type: GET_PODCAST_SUBSCRIPTION_SUCCESS,
        payload: {is_subscribed: response.data}
    })
}