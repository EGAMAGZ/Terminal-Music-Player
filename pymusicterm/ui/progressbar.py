from py_cui.widgets import Widget


class LoadingBarWidget(Widget):
    
    BAR_COMPLETED_CHAR=u'\u2588'

    def __init__(self,id,title,grid,row,column,row_span,column_span,padx,pady,logger) -> None:
        """ Initializer for LoadingBar Widget
        """
        super().__init__(id,title,grid,row,column,row_span,column_span,padx,pady,logger)
        self._draw_border=True
        self._num_items=10
        self._completed_items=0
        self._total_duration=title
        self._time_elapsed=title

    def increment(self):
        self._completed_items+=1

    def set_time_elapsed(self,time_elapsed:str):
        self._time_elapsed=time_elapsed


    def set_num_items(self,number_items):
        self._num_items=number_items

    def _draw(self):
        """ Override base draw class.
        """
        super()._draw()

        self._title="{}-{}".format(self._time_elapsed,self._total_duration)
        width=self._stop_x -self._start_x
        bar_width=width
        items_per_bar_block=self._num_items / bar_width
        bar_blocks_per_item=bar_width/self._num_items

        if items_per_bar_block >=1:
            completed_blocks=int(self._completed_items/items_per_bar_block)
        else:
            completed_blocks=int(bar_blocks_per_item * self._completed_items)

        non_completed_blocks= bar_width - completed_blocks

        text='{}{}'.format(self.BAR_COMPLETED_CHAR* completed_blocks,'-'*non_completed_blocks)
        self._renderer.set_color_mode(self._color)

        if self._draw_border:
            self._renderer.draw_border(self,with_title=True)
        target_y=self._start_y+int(self._height/2)

        self._renderer.draw_text(self,text,target_y,centered=True,bordered=self._draw_border)
        self._renderer.unset_color_mode(self._color)
        self._renderer.reset_cursor(self)
