import pytest

from jeoparpy.game.gamestate import (GameState, StateSetError, 
    StateTransitionError)

@pytest.fixture
def gs():
    """GameState object fixture"""
    dayStates = (
        'STATE0', 
        'STATE1',  
        'STATE2', 
        'STATE3',
        'STATE4',
    )
    
    return GameState(*dayStates)
    
def test_initial_state(gs):
    assert gs.state is None
    assert gs.previous is None
    assert gs.kwargs == {}
    
def test_previous(gs):
    # Change state multiple times, verifying previous each time
    assert gs.previous is None
    
    gs.state = gs.STATE0
    assert gs.previous is None
    
    gs.state = gs.STATE1
    assert gs.previous == gs.STATE0
    assert gs.previous == 0
    
    gs.set(gs.STATE2)
    assert gs.previous == gs.STATE1
    assert gs.previous == 1
    
    # Verify previous is read-only.
    with pytest.raises(AttributeError):
        gs.previous = gs.STATE3
        
def test_set(gs):
    gs.set(gs.STATE2)
    assert gs.state == gs.STATE2
    assert gs.state == 2
    
    gs.set(gs.STATE1, arg1=1)
    assert gs.state == gs.STATE1
    assert gs.state == 1
    assert gs.kwargs['arg1'] == 1
    
    with pytest.raises(StateTransitionError):
        gs.set(gs.STATE1)

    with pytest.raises(StateSetError):
        gs.set(-1)
    
def test_state_change(gs):
    gs.state = gs.STATE0
    assert gs.state == 0
    assert gs.state == gs.STATE0
    
    gs.state = gs.STATE2
    assert gs.state == 2
    assert gs.state == gs.STATE2
    
    gs.state = gs.STATE4
    assert gs.state == 4
    assert gs.state == gs.STATE4
    
    
def test_state_values(gs):
    assert gs.STATE0 == 0
    assert gs.STATE1 == 1
    assert gs.STATE2 == 2
    assert gs.STATE3 == 3
    assert gs.STATE4 == 4
    
def test_transition_errors(gs):
    gs.state = gs.STATE0
    
    with pytest.raises(StateTransitionError):
        gs.state = gs.STATE0
    
def test_kwargs(gs):
    assert gs.kwargs == {}
    
    gs.set(gs.STATE0, extraArg='test', extraArg2=5)
    assert len(gs.kwargs) == 2
    assert gs.kwargs['extraArg'] == 'test'
    assert gs.kwargs['extraArg2'] == 5
    
    # Verify previous kwargs clear via state.setter
    gs.state = gs.STATE3
    assert gs.kwargs == {}
    
    gs.set(gs.STATE1, extraArg='test', extraArg2=5)
    assert len(gs.kwargs) == 2
    assert gs.kwargs['extraArg'] == 'test'
    assert gs.kwargs['extraArg2'] == 5
    
    # Veridy previous args removed when setting with set()
    gs.set(gs.STATE4, arg1=1, arg2=2)
    assert len(gs.kwargs) == 2
    assert 'extraArg' not in gs.kwargs
    assert 'extraArg2' not in gs.kwargs
    assert gs.kwargs['arg1'] == 1
    assert gs.kwargs['arg2'] == 2
    
    # Verify previous args can be re-passed easily
    gs.set(gs.STATE1, **gs.kwargs)
