from py_cui.widgets import Widget


class LoadingBarWidget(Widget):
    
    BAR_COMPLETED_CHAR=u'\u2588'

    def __init__(self,id,title,grid,row,column,row_span,column_span,padx,pady,logger) -> None:
        super().__init__(id,title,grid,row,column,row_span,column_span,padx,pady,logger)
        self._draw_border=True
        self._num_items=10
        self._completed_items=9

    def _draw(self):
        super()._draw()

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
            self._renderer.draw_border(self,with_title=False)
        target_y=self._start_y+int(self._height/2)
        # self._renderer.draw_text(self,self._title,target_y-2,centered=True,bordered=self._draw_border)
        self._renderer.draw_text(self,text,target_y,centered=True,bordered=self._draw_border)
        self._renderer.unset_color_mode(self._color)
