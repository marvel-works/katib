// Code generated by MockGen. DO NOT EDIT.
// Source: github.com/kubeflow/katib/pkg/controller/v1alpha2/experiment/suggestion (interfaces: Suggestion)

// Package mock is a generated GoMock package.
package mock

import (
	gomock "github.com/golang/mock/gomock"
	v1alpha2 "github.com/kubeflow/katib/pkg/api/operators/apis/experiment/v1alpha2"
	v1alpha20 "github.com/kubeflow/katib/pkg/api/v1alpha2"
	reflect "reflect"
)

// MockSuggestion is a mock of Suggestion interface
type MockSuggestion struct {
	ctrl     *gomock.Controller
	recorder *MockSuggestionMockRecorder
}

// MockSuggestionMockRecorder is the mock recorder for MockSuggestion
type MockSuggestionMockRecorder struct {
	mock *MockSuggestion
}

// NewMockSuggestion creates a new mock instance
func NewMockSuggestion(ctrl *gomock.Controller) *MockSuggestion {
	mock := &MockSuggestion{ctrl: ctrl}
	mock.recorder = &MockSuggestionMockRecorder{mock}
	return mock
}

// EXPECT returns an object that allows the caller to indicate expected use
func (m *MockSuggestion) EXPECT() *MockSuggestionMockRecorder {
	return m.recorder
}

// GetSuggestions mocks base method
func (m *MockSuggestion) GetSuggestions(arg0 *v1alpha2.Experiment, arg1 int32) ([]*v1alpha20.Trial, error) {
	m.ctrl.T.Helper()
	ret := m.ctrl.Call(m, "GetSuggestions", arg0, arg1)
	ret0, _ := ret[0].([]*v1alpha20.Trial)
	ret1, _ := ret[1].(error)
	return ret0, ret1
}

// GetSuggestions indicates an expected call of GetSuggestions
func (mr *MockSuggestionMockRecorder) GetSuggestions(arg0, arg1 interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "GetSuggestions", reflect.TypeOf((*MockSuggestion)(nil).GetSuggestions), arg0, arg1)
}