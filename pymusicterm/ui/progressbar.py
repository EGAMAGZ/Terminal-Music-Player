from py_cui.widgets import Widget


class LoadingBarWidget(Widget):
    
    def __init__(self,id,title,grid,row,column,row_span,column_span,padx,pady,logger) -> None:
        super().__init__(id,title,grid,row,column,row_span,column_span,padx,pady,logger)
        self._draw_border=False

    def _draw(self):
        super()._draw()

        self._renderer.set_color_mode(self._color)

        if self._draw_border:
            self._renderer.draw_border(self,with_title=False)
        target_y=self._start_y+int(self._height/2)
        self._renderer.draw_text(self,self._title,target_y,centered=True,bordered=self._draw_border)
        self._renderer.unset_color_mode(self._color)
