"""
dashboard_layout
form_layout
preview_layout

button_layout
依照字數給定layout large medium small
依照 type 不過之後再做
"""

import json
import ipywidgets as widgets
from ast import literal_eval
from collections import OrderedDict
from .utility import string_to_list, list_to_string, most_common


class Annotator:
    """
    1. Initialize
    """
    def __init__(self, problems, custom_fields=None):
        
        self.problems = problems
        self.current_index = 0
        self.fileds = []
        self.fields = self._get_field_list()
        self.field_to_length, self.field_to_type = self._get_field_info()
        self._handle_custom_fields(custom_fields)
    
    def _get_field_list(self):
        """Get the field names in the data
        """
        all_fields = list()
        for problem in self.problems:
            fields = problem.keys()
            new_fields = [field for field in fields if field not in all_fields]
            all_fields = all_fields + new_fields
        return all_fields
    
    def _get_field_info(self):
        """
        """
        field_to_length = {}
        field_to_type = {}
        for field in self.fields:
            field_to_length[field] = max([len(str(prob[field])) for prob in self.problems if field in prob])
        for field in self.fields:
            field_to_type[field] = most_common([type(prob[field]) for prob in self.problems if field in prob])
        return field_to_length, field_to_type
    
    
    def _handle_custom_fields(self, custom_fields):
        for field, field_type, field_size in custom_fields:
            if field not in self.fields:
                self.fields.append(field)
                self.field_to_type[field] = field_type
                self.field_to_length[field] = field_size

        
    def start(self):
        self.initialize_dashboard()
        self.render_value()
    
    
    def initialize_dashboard(self):
  
        # Layouts
        layout_lg = widgets.Layout(flex='0 1 150px', height='100%', width='90%')
        layout_md = widgets.Layout(flex='0 1 50px', height='100%', width='90%')
        layout_sm = widgets.Layout(flex='0 1 20px', width='90%')        
 
        # Fields
        height = 0
        self.form_widgets = OrderedDict()
        for field in self.fields:
            if self.field_to_length[field] <= 20:
                layout = layout_sm
                height += 20
                self.form_widgets[field] = widgets.Text(description=f'{field.capitalize()}: ', layout=layout)
            elif self.field_to_length[field] <= 100:
                layout = layout_md
                height += 50
                self.form_widgets[field] = widgets.Textarea(description=f'{field.capitalize()}: ', layout=layout)
            else:
                layout = layout_lg
                height += 150
                self.form_widgets[field] = widgets.Textarea(description=f'{field.capitalize()}: ', layout=layout)
        
        # Buttons
        # Take reference from 
        prevbtn = widgets.Button(description='< Previous')
        nextbtn = widgets.Button(description='Next >')
        savebtn = widgets.Button(description='Save')
        restorebtn = widgets.Button(description='Restore')
        prevbtn.on_click(lambda _: self.change_index(-1))
        nextbtn.on_click(lambda _: self.change_index(1))
        savebtn.on_click(self.save)
        restorebtn.on_click(self.restore)
        
        buttons_layout = widgets.Layout(width='80%', height='35px')
        height += 35
        buttons = widgets.HBox([prevbtn, nextbtn, savebtn, restorebtn], layout=buttons_layout)

        # Dashboard
        form_layout = widgets.Layout(width='47%', justify_content ='space-around',  align_items='flex-end')
        self.form = widgets.VBox([*self.form_widgets.values(), buttons], layout=form_layout)
        
        out = widgets.interactive_output(self.display_annotations, self.form_widgets)
        preview_layout = widgets.Layout(width='43%')
        self.preview = widgets.VBox([out], layout=preview_layout)
        
        dashboard_layout = widgets.Layout(height=f'{height+16*len(self.fields)}px')
        self.dashboard = widgets.HBox([self.preview, self.form], layout=dashboard_layout)
        display(self.dashboard)

        
    def display_annotations(self, **form_widgets):
        """
        This is the function that reads in the values of the widgets and outputs them in a customized format.
        改成 field1, field2, field3
        """
        output = {}
        for field in self.fields:
            field_type = self.field_to_type[field]
            if field_type == list:
                output[field] = string_to_list(form_widgets[field])
            elif field_type == dict:
                output[field] = literal_eval(form_widgets[field])
            else:
                output[field] = form_widgets[field]
        print(json.dumps(output, indent=4))

        
    def render_value(self):
        """
        """
        current_problem = self.problems[self.current_index]
        for field in self.fields:
            field_type = self.field_to_type[field]
            if field_type==list:
                self.form_widgets[field].value = list_to_string(current_problem[field]) if field in current_problem else ""
            elif field_type==dict:
                self.form_widgets[field].value = str(current_problem[field]) if field in current_problem else '{}'
            else:
                self.form_widgets[field].value = current_problem[field] if field in current_problem else ""
 
 
    def change_index(self, change):
        if change < 0 < self.current_index:
            self.current_index -= 1
        elif change > 0 and self.current_index < len(self.problems) -1:
            self.current_index += 1
        self.render_value()
            
            
    def save(self, change):
        current_problem = self.problems[self.current_index]
        for field in self.fields:
            field_type = self.field_to_type[field]
            if field_type == list:
                current_problem[field] = string_to_list(self.form_widgets[field].value)
            elif field_type == dict:
                current_problem[field] = literal_eval(self.form_widgets[field].value)
            else:
                current_problem[field] = self.form_widgets[field].value
        
    def restore(self, change):
        self.render_value()