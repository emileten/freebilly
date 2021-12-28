import abc
from pathlib import Path
from typing import Tuple
from src.freebilly.repository.AbstractRepository import AbstractRepository
from src.freebilly.domain.AbstractWorkLog import AbstractWorkLog
from src.freebilly.domain.AbstractWorkSession import AbstractWorkSession

class AbstractServiceLayer(abc.ABC):

    """
    abstraction over the layer where 'services' are performed : jobs that can be identified to what a user actually
    needs to do with work sessions and work logs.
    """

    @abc.abstractmethod
    def start_session(self, path: Path, client: str, project: str) -> Tuple[AbstractRepository, AbstractWorkLog, AbstractWorkSession]:

        """
        Starts a work session and provides the objects needed to manage it.

        Parameters
        ----------
        path: Path
        client: str
        project: str

        Returns
        -------
        Tuple[AbstractRepository, AbstractWorkLog, AbstractWorkSession]
            Objects to handle the new session.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def end_session(self, repo: AbstractRepository, work_log: AbstractWorkLog, work_session: AbstractWorkSession) -> None:

        """
        Ends a work session by adding it to some work log and pushing that to some repository.
        
        Parameters
        ----------
        repo: AbstractRepository
        work_log: AbstractWorkLog
        work_session: AbstractWorkSession
        """
        raise NotImplementedError